import http
from collections.abc import Callable
from json import dumps
from types import MappingProxyType
from typing import Any, Literal
from urllib.parse import urljoin, urlparse, urlunparse

import msgspec.json
from aiohttp import ClientResponse, ClientSession

from async_tensorart.__meta__ import __version__
from async_tensorart.base import BaseTensorArt
from async_tensorart.exceptions import (
    TensorArtBadGatewayError,
    TensorArtBadRequestError,
    TensorArtError,
    TensorArtForbiddenError,
    TensorArtInternalServerError,
    TensorArtNotFoundError,
    TensorArtServiceUnavailableError,
    TensorArtTooManyRequestsError,
    TensorArtUnauthorizedError,
    TensorArtUnknownError,
)
from async_tensorart.signature import PrivateKey, generate_signature
from async_tensorart.structs.jobs.delete.job import DelJob
from async_tensorart.structs.jobs.get.job import JobAnswer, JobDict
from async_tensorart.structs.jobs.post.job import PostJob
from async_tensorart.structs.models.model import Model, ModelDict


class TensorArt(BaseTensorArt):
    headers: MappingProxyType = MappingProxyType(
        {
            "Content-Type": "application/json",
            "User-Agent": f"TensorArt Python Client/{__version__}",
            "Accept": "application/json",
        },
    )

    def __init__(
        self,
        app_id: str,
        endpoint: str,
        session: ClientSession,
        private_key: PrivateKey,
        *,
        api_version: int = 1,
        json_encoder: Callable[[Any], str | bytes] = dumps,
        # json_decoder: Callable[[str | bytes], Any] = loads,
    ) -> None:
        self.app_id = app_id
        self.endpoint = endpoint
        self.session = session
        self.private_key = private_key
        self.api_version = api_version
        self.json_encoder = json_encoder

        # self.session.__setattr__("_json_serialize", self.json_encoder)

        if (url := urlparse(endpoint)).scheme not in {"http", "https"}:
            self.endpoint = urlunparse(
                ("https", url.path, f"v{self.api_version}/", *url[3:]),
            )

    async def _request(
        self,
        method: Literal["GET", "POST", "DELETE"],
        path: str,
        json: dict | None = None,
        **kwargs,
    ) -> bytes:
        signature = generate_signature(
            app_id=self.app_id,
            method=method,
            url=urljoin(f"/v{self.api_version}/", path),
            body=self.json_encoder(json) if json is not None else None,
            private_key=self.private_key,
            nonce=kwargs.get("nonce"),
        )

        async with self.session.request(
            method,
            urljoin(self.endpoint, path),
            headers={
                **self.headers,
                "Authorization": signature,
            },
            json=json,
            **kwargs,
        ) as r:
            status, error = self._check_status(r.status)

            if status:
                return await self._process_response(r)

            raise (
                error(
                    code=r.status,
                    remote_message=await r.text(),
                )
                if error is not None
                else TensorArtError(
                    code=r.status,
                    remote_message=await r.text(),
                )
            )

    @staticmethod
    def _check_status(status: int) -> tuple[bool, type[TensorArtError] | None]:
        match status:
            case http.HTTPStatus.OK:
                return True, None
            case http.HTTPStatus.ACCEPTED:
                return True, None
            case http.HTTPStatus.BAD_REQUEST:
                return False, TensorArtBadRequestError
            case http.HTTPStatus.UNAUTHORIZED:
                return False, TensorArtUnauthorizedError
            case http.HTTPStatus.FORBIDDEN:
                return False, TensorArtForbiddenError
            case http.HTTPStatus.NOT_FOUND:
                return False, TensorArtNotFoundError
            case http.HTTPStatus.TOO_MANY_REQUESTS:
                return False, TensorArtTooManyRequestsError
            case http.HTTPStatus.INTERNAL_SERVER_ERROR:
                return False, TensorArtInternalServerError
            case http.HTTPStatus.BAD_GATEWAY:
                return False, TensorArtBadGatewayError
            case http.HTTPStatus.SERVICE_UNAVAILABLE:
                return False, TensorArtServiceUnavailableError
            case _:
                return False, TensorArtUnknownError

    async def _process_response(self, response: ClientResponse) -> bytes:
        return await response.read()

    async def get_job(self, job_id: int | str) -> JobAnswer | None:
        result = await self._request("GET", urljoin("jobs/", str(job_id)))
        if result is not None:
            return msgspec.json.decode(result, type=JobDict).job
        return None

    async def post_job(self, job: PostJob) -> JobAnswer | None:
        result = await self._request(
            "POST",
            "jobs",
            json=msgspec.to_builtins(job),
        )
        if result is not None:
            return msgspec.json.decode(result, type=JobDict).job
        return None

    async def del_job(self, job_id: int | str) -> DelJob | None:
        result = await self._request("DELETE", urljoin("jobs/", str(job_id)))
        if result is not None:
            return msgspec.json.decode(result, type=DelJob)
        return None

    async def get_model(self, model_id: int) -> Model | None:
        result = await self._request("GET", urljoin("models/", str(model_id)))
        if result is not None:
            return msgspec.json.decode(result, type=ModelDict).model
        return None
