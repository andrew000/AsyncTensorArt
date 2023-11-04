from collections.abc import Sequence

from msgspec import UNSET, Struct, UnsetType

from async_tensorart.structs.jobs.post.stage import Stage


class PostJob(Struct, kw_only=True):
    request_id: str
    stages: Sequence[Stage]
    notify_url: str | UnsetType = UNSET
