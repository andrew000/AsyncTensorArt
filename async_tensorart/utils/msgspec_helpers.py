from typing import Any

import msgspec


def msgspec_encode(data: dict[str, Any]) -> str:
    return msgspec.json.encode(data).decode("utf-8")
