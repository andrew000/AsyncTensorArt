from msgspec import Struct, field


class LoraItem(Struct, kw_only=True):
    lora_model: str = field(name="loraModel")
    """The model to use for the diffusion, `How to get the model id <
    https://tams-docs.tensor.art/docs/api/guide/how-to-get-the-model-id>`_"""
    weight: float = field(name="weight")
    block_weight: str = field(name="blockWeight")
    """lora block weight, value such as <weight>:lbw=<layer weight>
    example: '1:lbw=1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0'"""


class Lora(Struct, kw_only=True):
    items: list[LoraItem] = field(name="items", default=[])
