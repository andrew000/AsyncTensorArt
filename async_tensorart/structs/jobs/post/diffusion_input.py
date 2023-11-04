from collections.abc import Sequence

from msgspec import UNSET, Struct, UnsetType, field

from async_tensorart.structs.jobs.post.animate_diff import AnimateDiff
from async_tensorart.structs.jobs.post.control_net import ControlNet
from async_tensorart.structs.jobs.post.enums import VAE, Sampler
from async_tensorart.structs.jobs.post.lora import Lora


class Prompt(Struct, kw_only=True):
    """Prompt for the `diffusion` stage type."""

    text: str
    """Text prompt."""
    weight: float


class DiffusionInput(Struct, kw_only=True):
    width: int = field(name="width", default=512)
    """Height of the image in pixels. Must be in increments of 64 and pass the
    following validation:

    * For 512 engines: 262,144 ≤ height * width ≤ 1,048,576, Maximum 1024
    * For 768 engines: 589,824 ≤ height * width ≤ 1,048,576, Maximum 1024
    * For SDXL v1.0: 262,144 ≤ height * width ≤ 2,073,600, Maximum 1536
    """
    height: int = field(name="height", default=512)
    """Height of the image in pixels. Must be in increments of 64 and pass the
    following validation:

    * For 512 engines: 262,144 ≤ height * width ≤ 1,048,576, Maximum 1024
    * For 768 engines: 589,824 ≤ height * width ≤ 1,048,576, Maximum 1024
    * For SDXL v1.0: 262,144 ≤ height * width ≤ 2,073,600, Maximum 1536
    """
    prompts: Sequence[Prompt] = field(name="prompts", default=[])
    """An array of text prompts to use for generation. Given a text prompt with the
    text A lighthouse on a cliff and a weight of 0.5, it would be represented as:"""
    negative_prompts: Sequence[Prompt] = field(name="negativePrompts", default=[])
    """An array of text negative prompts to use for generation. Given a text prompt
    with the text A lighthouse on a cliff and a weight of 0.5, it would be
    represented as:"""
    sd_model: str | UnsetType = field(name="sdModel", default=UNSET)
    """The model to use for the diffusion, `How to get the model id
    <https://tams-docs.tensor.art/docs/api/guide/how-to-get-the-model-id>`_"""
    sd_vae: VAE | UnsetType = field(name="sdVae", default=UNSET)
    """The vae to use for the diffusion `Support list
    <https://tams-docs.tensor.art/docs/api/guide/list-of-constants#vae>`_"""
    sampler: Sampler | UnsetType = field(name="sampler", default=UNSET)
    """Which sampler to use for the diffusion process. If this value is omitted we'll
    automatically select an appropriate sampler for you. `Support list
    <https://tams-docs.tensor.art/docs/api/guide/list-of-constants#sampler>`_"""
    steps: int = field(name="steps", default=0)
    """Number of diffusion steps to run."""
    cfg_scale: float = field(name="cfgScale", default=7.0)
    """How strictly the diffusion process adheres to the prompt text (higher values
    keep your image closer to your prompt)"""
    clip_skip: int = field(name="clipSkip", default=1)
    denoising_strength: float | UnsetType = field(
        name="denoisingStrength",
        default=UNSET,
    )
    eta_noise_seed_delta: int | UnsetType = field(
        name="etaNoiseSeedDelta",
        default=UNSET,
    )
    control_net: ControlNet | UnsetType = field(name="controlNet", default=UNSET)
    lora: Lora | UnsetType = field(name="lora", default=UNSET)
    animate_diff: AnimateDiff | UnsetType = field(name="animateDiff", default=UNSET)
