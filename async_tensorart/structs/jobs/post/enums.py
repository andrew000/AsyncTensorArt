from enum import Enum


class StageTypeT(Enum):
    DEFAULT = "DEFAULT"
    INPUT_INITIALIZE = "INPUT_INITIALIZE"
    DIFFUSION = "DIFFUSION"
    IMAGE_TO_UPSCALER = "IMAGE_TO_UPSCALER"
    IMAGE_TO_ADETAILER = "IMAGE_TO_ADETAILER"
    IMAGE_TO_INPAINT = "IMAGE_TO_INPAINT"
    IMAGE_TO_ANIMATE_DIFF = "IMAGE_TO_ANIMATE_DIFF"


class VAE(Enum):
    AUTOMATIC = "Automatic"
    VAE_FT_MSE_840000_EMA_PRUNED = "vae-ft-mse-840000-ema-pruned.ckpt"
    KL_F8_ANIME = "kl-f8-anime.ckpt"
    KL_F8_ANIME2 = "kl-f8-anime2.ckpt"
    YOZORA = "yozora.vae.pt"
    ORANGEMIX = "orangemix.vae.pt"
    BLESSED2 = "blessed2.vae.pt"
    ANIMEVAE = "animevae.pt"
    CLEARVAE = "clearvae.safetensor"
    PASTER_WAIFU_DIFFUSION = "paster-waifu-diffusion.vae.pt"


class Sampler(Enum):
    EULER_A = "Euler_a"
    Euler = "Euler"
    LMS = "LMS"
    Heun = "Heun"
    DPM2 = "DPM2"
    DPM2_A = "DPM2 a"
    DPM_PP_2S_A = "DPM++ 2S a"
    DPM_PP_2M = "DPM++ 2M"
    DPM_PP_SDE = "DPM++ SDE"
    DPM_PP_2M_SDE = "DPM++ 2M SDE"
    DPM_FAST = "DPM fast"
    LMS_KARRAS = "LMS Karras"
    DPM2_KARRAS = "DPM2 Karras"
    DPM2_A_KARRAS = "DPM2 a Karras"
    DPM_PP_2S_A_KARRAS = "DPM++ 2S a Karras"
    DPM_PP_2M_KARRAS = "DPM++ 2M Karras"
    DPM_PP_SDE_KARRAS = "DPM++ SDE Karras"
    DPM_PP_2M_SDE_KARRAS = "DPM++ 2M SDE Karras"


class ControlnetArgsResizeModeT(Enum):
    DEFAULT = "DEFAULT"
    JUST_RESIZE = "JUST_RESIZE"
    CROP_AND_RESIZE = "CROP_AND_RESIZE"
    RESIZE_AND_FILL = "RESIZE_AND_FILL"


class ArgsControlModeT(Enum):
    DEFAULT = "DEFAULT"
    BALANCED = "BALANCED"
    MY_PROMPT_IS_MORE_IMPORTANT = "MY_PROMPT_IS_MORE_IMPORTANT"
    CONTROLNET_IS_MORE_IMPORTANT = "CONTROLNET_IS_MORE_IMPORTANT"


class ImageToInpaintInputResizeModeT(Enum):
    DEFAULT = "DEFAULT"
    JUST_RESIZE = "JUST_RESIZE"
    CROP_AND_RESIZE = "CROP_AND_RESIZE"
    RESIZE_AND_FILL = "RESIZE_AND_FILL"
    JUST_RESIZE_LATENT_UPSCALE = "JUST_RESIZE_LATENT_UPSCALE"


class ImageToInpaintInputInpaintFillT(Enum):
    DEFAULT = "DEFAULT"
    FILL = "FILL"
    ORIGINAL = "ORIGINAL"
    LATENT_NOISE = "LATENT_NOISE"
    LATENT_NOTHING = "LATENT_NOTHING"
