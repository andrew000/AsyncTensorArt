from collections.abc import Sequence

from msgspec import Struct, field


class ResourceForClient(Struct, kw_only=True):
    id: str
    url: str
    expired_in: str = field(name="expiredIn")


class ProcessingImage(Struct, kw_only=True):
    resource_image: ResourceForClient = field(name="resourceImage")
    progress: int


class StageInfo(Struct, kw_only=True):
    stage_index: int = field(name="stageIndex")
    processing_images: Sequence[ProcessingImage] = field(name="processingImages")
