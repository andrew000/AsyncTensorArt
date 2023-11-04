from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.get.status import (
    FailedInfo,
    RunningInfo,
    Status,
    SuccessInfo,
    WaitingInfo,
)


class JobAnswer(Struct, kw_only=True):
    id: str
    status: Status = field(name="status", default=Status.DEFAULT)
    waiting_info: WaitingInfo | UnsetType = field(name="waitingInfo", default=UNSET)
    failed_info: FailedInfo | UnsetType = field(name="failedInfo", default=UNSET)
    running_info: RunningInfo | UnsetType = field(name="runningInfo", default=UNSET)
    success_info: SuccessInfo | UnsetType = field(name="successInfo", default=UNSET)


class JobDict(Struct, kw_only=True):
    """Response from GET /jobs/{job_id}."""

    job: JobAnswer
