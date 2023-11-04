from collections.abc import Sequence
from enum import Enum

from msgspec import UNSET, Struct, UnsetType, field


class ModelType(Enum):
    DEFAULT = "DEFAULT"
    CHECKPOINT = "CHECKPOINT"
    TEXTUAL_INVERSION = "TEXTUAL_INVERSION"
    HYPERNETWORK = "HYPERNETWORK"
    AESTHETIC_GRADIENT = "AESTHETIC_GRADIENT"
    LORA = "LORA"
    LOCON = "LOCON"
    CONTROLNET = "CONTROLNET"
    POSES = "POSES"
    WILDCARDS = "WILDCARDS"
    OTHER = "OTHER"
    LYCORIS = "LYCORIS"


class Model(Struct, kw_only=True):
    id: str
    name: str
    description: str
    base_model: str = field(name="baseModel")
    model_type: ModelType = field(name="modelType")
    showcase_image_urls: Sequence[str] = field(name="showcaseImageUrls")
    project_name: str = field(name="projectName")
    trigger_words: str | UnsetType = field(name="triggerWords", default=UNSET)


class ModelDict(Struct, kw_only=True):
    model: Model
