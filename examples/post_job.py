import asyncio
from pathlib import Path
from uuid import uuid4

import environs
from aiohttp import ClientSession
from async_tensorart import PrivateKey, TensorArt
from async_tensorart.structs.jobs.post.diffusion import Diffusion, Prompt
from async_tensorart.structs.jobs.post.enums import Sampler, StageType
from async_tensorart.structs.jobs.post.job import PostJob
from async_tensorart.structs.jobs.post.stage import InputInitialize, Stage

env = environs.Env()
env.read_env()


async def post_job() -> None:
    model_id: int = 42  # You can find this on the website.

    tensor = TensorArt(
        app_id=env.str("APP_ID"),
        endpoint=env.str("ENDPOINT"),
        session=ClientSession(),
        private_key=PrivateKey(
            path=Path("private_key.pem"),
            passphrase=env.str("PK_PASSPHRASE") or None,
        ),
    )

    stage_1 = Stage(
        type=StageType.INPUT_INITIALIZE,
        input_initialize=InputInitialize(
            seed=0,
            count=1,
        ),
    )

    stage_2 = Stage(
        type=StageType.DIFFUSION,
        diffusion=Diffusion(
            width=512,
            height=512,
            prompts=[
                Prompt(
                    text="1girl, standing, simple background, blue hair, blue eyes, "
                    "looking at viewer, twintails, open mouth, hair between eye",
                    weight=1.0,
                ),
            ],
            sd_model=str(model_id),
            sampler=Sampler.DPM_PP_2M_KARRAS,
            steps=20,
            clip_skip=2,
        ),
    )

    job = PostJob(request_id=uuid4().hex, stages=(stage_1, stage_2))
    result = await tensor.post_job(job)
    print(result)  # noqa: T201


asyncio.run(post_job())
