from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.diffusion_input import DiffusionInput, Prompt
from async_tensorart.structs.jobs.post.lora import Lora


class AdetailerArg(Struct, kw_only=True):
    ad_model: str = field(name="adModel")
    ad_prompt: list[Prompt] = field(name="adPrompt", default=[])
    ad_negative_prompt: list[Prompt] = field(name="adNegativePrompt", default=[])
    ad_confidence: float | UnsetType = field(name="adConfidence", default=UNSET)
    ad_dilate_erode: int = field(name="adDilateErode", default=4)
    ad_mask_merge_invert: str = field(name="adMaskMergeInvert", default="None")
    ad_denoising_strength: float = field(name="adDenoisingStrength", default=0.4)
    ad_inpaint_only_masked: bool = field(name="adInpaintOnlyMasked", default=True)
    ad_inpaint_only_masked_padding: float = field(
        name="adInpaintOnlyMaskedPadding",
        default=32.0,
    )
    ad_use_inpaint_width_height: bool = field(
        name="adUseInpaintWidthHeight",
        default=False,
    )
    ad_inpaint_width: int = field(name="adInpaintWidth", default=512)
    ad_inpaint_height: int = field(name="adInpaintHeight", default=512)
    ad_use_steps: bool = field(name="adUseSteps", default=False)
    ad_steps: int = field(name="adSteps", default=20)
    ad_use_cfg_scale: bool = field(name="adUseCfgScale", default=False)
    ad_cfg_scale: float = field(name="adCfgScale", default=7.0)
    lora: Lora | UnsetType = field(name="lora", default=UNSET)
    ad_use_checkpoint: bool | UnsetType = field(name="adUseCheckpoint", default=UNSET)
    ad_checkpoint: str | UnsetType = field(name="adCheckpoint", default=UNSET)
    ad_use_sampler: bool | UnsetType = field(name="adUseSampler", default=UNSET)
    ad_use_noise_multiplier: bool | UnsetType = field(
        name="adUseNoiseMultiplier",
        default=UNSET,
    )
    ad_noise_multiplier: float | UnsetType = field(
        name="adNoiseMultiplier",
        default=UNSET,
    )
    ad_use_clip_skip: bool | UnsetType = field(name="adUseClipSkip", default=UNSET)
    ad_clip_skip: int | UnsetType = field(name="adClipSkip", default=UNSET)
    ad_sampler: str | UnsetType = field(name="adSampler", default=UNSET)


class ImageToAdetailerInput(Struct, kw_only=True):
    args: list[AdetailerArg] = field(name="args", default=[])
    diffusion: DiffusionInput | UnsetType = field(name="diffusion", default=UNSET)
