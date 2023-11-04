from collections.abc import Sequence
from enum import Enum

from msgspec import Struct, field

from async_tensorart.structs.jobs.get.stage import ResourceForClient, StageInfo


class Status(Enum):
    DEFAULT = "DEFAULT"
    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CANCELED = "CANCELED"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    WAITING = "WAITING"


class WaitingInfo(Struct, kw_only=True):
    queue_rank: str


class FailedInfo(Struct, kw_only=True):
    reason: str
    stages: Sequence[StageInfo] = field(name="stages", default=[])


class RunningInfo(Struct, kw_only=True):
    stages: Sequence[StageInfo] = field(name="stages", default=[])


class SuccessInfo(Struct, kw_only=True):
    images: Sequence[ResourceForClient] = field(name="images", default=[])
    stages: Sequence[StageInfo] = field(name="stages", default=[])
    videos: Sequence[ResourceForClient] = field(name="videos", default=[])
