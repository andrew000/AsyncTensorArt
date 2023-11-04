from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.enums import (
    ArgsControlModeT,
    ControlnetArgsResizeModeT,
)


class ControlnetArgs(Struct, kw_only=True):
    input_image_resource_id: str | UnsetType = field(
        name="inputImageResourceId",
        default=UNSET,
    )
    mask_resource_id: str | UnsetType = field(name="maskResourceId", default=UNSET)
    preprocessor: str = field(name="preprocessor")
    """The model to use for the controlnet preprocessor `Support list
    <https://tams-docs.tensor.art/docs/api/guide/list-of-constants#preprocessor>`_"""
    model: str = field(name="model")
    """The model to use for the controlnet `Support list
    <https://tams-docs.tensor.art/docs/api/guide/list-of-constants#model-1>`_"""
    weight: float | UnsetType = field(name="weight", default=UNSET)
    resize_mode: ControlnetArgsResizeModeT | UnsetType = field(
        name="resizeMode",
        default=UNSET,
    )
    guidance: float | UnsetType = field(name="guidance", default=UNSET)
    guidance_start: float | UnsetType = field(name="guidanceStart", default=UNSET)
    guidance_end: float | UnsetType = field(name="guidanceEnd", default=UNSET)
    control_mode: ArgsControlModeT | UnsetType = field(
        name="controlMode",
        default=UNSET,
    )
    pixel_perfect: bool | UnsetType = field(name="pixelPerfect", default=UNSET)
    preprocessor_params: dict[str, str] | UnsetType = field(
        name="preprocessorParams",
        default=UNSET,
    )


class ControlNet(Struct, kw_only=True):
    args: list[ControlnetArgs] = field(name="args", default=[])
