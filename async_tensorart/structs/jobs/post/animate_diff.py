from msgspec import Struct, field


class AnimateDiffArg(Struct, kw_only=True):
    video_length: int = field(name="videoLength")
    fps: int = field(name="fps")


class AnimateDiff(Struct, kw_only=True):
    args: list[AnimateDiffArg] = field(name="args", default=[])
