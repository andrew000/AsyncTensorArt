from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.diffusion_input import DiffusionInput


class ImageToUpscalerInput(Struct, kw_only=True):
    hr_upscaler: str
    """The model to use for the upscaling `Support list
    <https://tams-docs.tensor.art/docs/api/guide/list-of-constants#upscaler>`_"""
    hr_resize_x: int | UnsetType = field(name="hrResizeX", default=UNSET)
    """*Optional*. hr_scale or hr_resize_x must be specified. If hr_scale is
    specified, hr_resize_x will be ignored. Height of the image upscaler in pixels.
    Must be in increments of 64 and pass the following validation:
    * 262,144 ≤ hr_resize_x * hr_resize_y ≤ 8,294,400"""
    hr_resize_y: int | UnsetType = field(name="hrResizeY", default=UNSET)
    """*Optional*. hr_scale or hr_resize_y must be specified. If hr_scale is
    specified, hr_resize_y will be ignored. Height of the image upscaler in pixels.
    Must be in increments of 64 and pass the following validation:
    * 262,144 ≤ hr_resize_x * hr_resize_y ≤ 8,294,400"""
    hr_scale: float | UnsetType = field(name="hrScale", default=UNSET)
    """*Optional*. The size to use for the upscaling
    * 262,144 ≤ hr_resize_x * hr_resize_y ≤ 8,294,400"""
    hr_second_pass_steps: int = field(name="hrSecondPassSteps")
    """Number of diffusion steps to run."""
    denoising_strength: float = field(name="denoisingStrength")
    """denoising_strength"""
    diffusion: DiffusionInput | UnsetType = field(name="diffusion", default=UNSET)
    """*Optional*. Diffusion parameters."""
