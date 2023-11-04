from msgspec import Struct


class DelJob(Struct, kw_only=True):
    """Represents a job deletion request."""

    job_id: str
