from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.diffusion_input import DiffusionInput
from async_tensorart.structs.jobs.post.enums import StageTypeT
from async_tensorart.structs.jobs.post.image_to_adetailer import ImageToAdetailerInput
from async_tensorart.structs.jobs.post.image_to_inpaint import ImageToInpaint
from async_tensorart.structs.jobs.post.image_to_upscaler import ImageToUpscalerInput


class InputInitializeInput(Struct, kw_only=True):
    """Input for the `inputInitialize` stage type."""

    seed: int = field(name="seed", default=0)
    """Random noise seed (omit this option or use 0 for a random seed)."""
    image_resource_id: str | UnsetType = field(name="imageResourceId", default=UNSET)
    """Image used to initialize the diffusion process, in lieu of random noise."""
    count: int = field(name="count", default=1)
    """Number of images to generate"""


class CreateJobRequestStage(Struct, kw_only=True):
    type: StageTypeT = field(name="type", default=StageTypeT.DEFAULT)
    """Stage type."""
    input_initialize: InputInitializeInput | UnsetType = field(
        name="inputInitialize",
        default=UNSET,
    )
    """*Optional*. Input for the `inputInitialize` stage type."""
    diffusion: DiffusionInput | UnsetType = field(name="diffusion", default=UNSET)
    image_to_upscaler: ImageToUpscalerInput | UnsetType = field(
        name="imageToUpscaler",
        default=UNSET,
    )
    image_to_adetailer: ImageToAdetailerInput | UnsetType = field(
        name="imageToAdetailer",
        default=UNSET,
    )
    image_to_inpaint: ImageToInpaint | UnsetType = field(
        name="imageToInpaint",
        default=UNSET,
    )
