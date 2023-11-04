from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.diffusion_input import DiffusionInput
from async_tensorart.structs.jobs.post.enums import (
    ImageToInpaintInputInpaintFillT,
    ImageToInpaintInputResizeModeT,
)


class ImageToInpaint(Struct, kw_only=True):
    resize_mode: ImageToInpaintInputResizeModeT = field(
        name="resizeMode",
        default=ImageToInpaintInputResizeModeT.DEFAULT,
    )
    mask_image_resource_id: str | UnsetType = field(
        name="maskImageResourceId",
        default=UNSET,
    )
    mask_blur: float = field(name="maskBlur", default=4.0)
    inpainting_fill: ImageToInpaintInputInpaintFillT = field(
        name="inpaintingFill",
        default=ImageToInpaintInputInpaintFillT.DEFAULT,
    )
    inpaint_full_res: bool = field(name="inpaintFullRes", default=True)
    inpaint_full_res_padding: int = field(name="inpaintFullResPadding", default=32)
    inpaint_mask_invert: int = field(name="inpaintMaskInvert", default=0)
    diffusion: DiffusionInput | UnsetType = field(name="diffusion", default=UNSET)
