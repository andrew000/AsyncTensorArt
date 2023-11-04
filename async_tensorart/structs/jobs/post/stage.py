from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.diffusion import Diffusion
from async_tensorart.structs.jobs.post.enums import StageType


class InputInitialize(Struct, kw_only=True):
    """Input for the `inputInitialize` stage type."""

    seed: int = field(name="seed", default=0)
    """Random noise seed (omit this option or use 0 for a random seed)."""
    image_resource_id: str | UnsetType = field(name="imageResourceId", default=UNSET)
    """Image used to initialize the diffusion process, in lieu of random noise."""
    count: int = field(name="count", default=1)
    """Number of images to generate"""


class Stage(Struct, kw_only=True):
    type: StageType = field(name="type", default=StageType.DEFAULT)
    """Stage type."""
    input_initialize: InputInitialize | UnsetType = field(
        name="inputInitialize",
        default=UNSET,
    )
    """*Optional*. Input for the `inputInitialize` stage type."""
    diffusion: Diffusion | UnsetType = field(name="diffusion", default=UNSET)
    # image_to_upscaler: ImageToUpscaler | None = field(name="imageToUpscaler",
    # default=None) image_to_adetailer: ImageToAdetailer | None = field(
    # name="imageToAdetailer", default=None) image_to_inpaint: ImageToInpaint | None
    # = field(name="imageToInpaint", default=None)
