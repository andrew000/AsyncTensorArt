import asyncio
from pathlib import Path

import environs
from aiohttp import ClientSession
from async_tensorart import PrivateKey, TensorArt

env = environs.Env()
env.read_env()


async def get_model() -> None:
    model_id: int = 1

    tensor = TensorArt(
        app_id=env.str("APP_ID"),
        endpoint=env.str("ENDPOINT"),
        session=ClientSession(),
        private_key=PrivateKey(
            path=Path("private_key.pem"),
            passphrase=env.str("PK_PASSPHRASE") or None,
        ),
    )

    result = await tensor.get_model(model_id)
    print(result)  # noqa: T201


asyncio.run(get_model())
