from base64 import b64encode
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal
from uuid import uuid4

from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import load_pem_private_key


class PrivateKey:
    def __init__(
        self,
        path: Path,
        passphrase: str | Path | None = None,
    ) -> None:
        self.path = path
        self.private_key = self.read_key(passphrase)

    def read_key(
        self,
        passphrase: str | bytes | Path | None = None,
    ) -> RSAPrivateKey:
        if isinstance(passphrase, str):
            passphrase = passphrase.encode("utf-8")

        elif isinstance(passphrase, Path):
            passphrase = passphrase.read_bytes()

        return load_pem_private_key(
            data=self.path.read_bytes(),
            password=passphrase,
        )  # type: ignore[return-value]

    def sign(self, data: str | bytes) -> str:
        if isinstance(data, str):
            data = data.encode("utf-8")

        signature = self.private_key.sign(  # type: ignore[call-arg,union-attr]
            data=data,
            padding=PKCS1v15(),
            algorithm=SHA256(),
        )
        return b64encode(signature).decode("utf-8")

    def __call__(self, data: str | bytes) -> str:
        return self.sign(data)


def generate_signature(
    app_id: str,
    method: Literal["GET", "POST", "DELETE"],
    url: str,
    private_key: PrivateKey,
    timestamp: int | datetime | None = None,
    body: str | bytes | None = None,
    nonce: str | None = None,
) -> str:
    if isinstance(timestamp, datetime):
        timestamp = int(timestamp.timestamp())

    elif timestamp is None:
        timestamp = int(datetime.now(tz=timezone.utc).timestamp())

    if isinstance(body, bytes):
        body = body.decode("utf-8")

    elif body is None:
        body = ""

    if nonce is None:
        nonce = uuid4().hex

    signature = private_key(f"{method}\n{url}\n{timestamp}\n{nonce}\n{body}")

    return (
        f"TAMS-SHA256-RSA "
        f"app_id={app_id},"
        f"nonce_str={nonce},"
        f"timestamp={timestamp},"
        f"signature={signature}"
    )
