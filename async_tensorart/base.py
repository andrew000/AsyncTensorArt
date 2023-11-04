from abc import ABC, abstractmethod
from collections.abc import Callable
from types import MappingProxyType
from typing import Any, Literal


class BaseTensorArt(ABC):
    headers: MappingProxyType

    @abstractmethod
    def __init__(
        self,
        app_id: str,
        endpoint: str,
        session: Any,
        *,
        json_encoder: Callable[[Any], str | bytes],
        json_decoder: Callable[[str | bytes], Any],
    ) -> None:
        ...

    @abstractmethod
    async def _request(
        self,
        method: Literal["GET", "POST", "DELETE"],
        path: str,
        json: dict | None = None,
        **kwargs,
    ) -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def _check_status(status: int) -> tuple[bool, type[Exception] | None]:
        ...

    @abstractmethod
    async def _process_response(self, response: Any) -> bytes:
        ...
