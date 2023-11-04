from collections.abc import Sequence

from msgspec import UNSET, Struct, UnsetType

from async_tensorart.structs.jobs.post.stage import CreateJobRequestStage


class PostJob(Struct, kw_only=True):
    request_id: str
    stages: Sequence[CreateJobRequestStage]
    notify_url: str | UnsetType = UNSET
