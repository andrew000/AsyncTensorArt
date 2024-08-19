from collections.abc import AsyncIterator, Callable
from pathlib import Path

import pytest
from aiohttp import ClientSession
from async_tensorart import PrivateKey, TensorArt


@pytest.fixture(scope="module")
async def aiohttp_client_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as session:
        yield session


class MockPrivateKey(PrivateKey):
    def read_key(
        self,
        passphrase: str | Path | None = None,
    ) -> None:
        pass


@pytest.fixture(scope="module", name="private_key")
def private_key_fixture() -> Callable[..., MockPrivateKey]:
    def _private_key(
        path: Path,
        passphrase: str | Path | None = None,
    ) -> MockPrivateKey:
        return MockPrivateKey(
            path=path,
            passphrase=passphrase,
        )

    return _private_key


@pytest.mark.asyncio
async def test_client_creation(
    aiohttp_client_session: ClientSession,
    private_key: Callable[..., PrivateKey],
) -> None:
    client = TensorArt(
        app_id="42",
        endpoint="abc123.tensorart.cloud",
        session=aiohttp_client_session,
        private_key=private_key(
            path=Path("private_key.pem"),
            passphrase=Path("passphrase.txt"),
        ),
    )
    assert client.session == aiohttp_client_session
