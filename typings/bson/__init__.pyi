from typing import Any

from bson.codec_options import CodecOptions
from bson.objectid import ObjectId
from bson.son import SON

def decode_iter(data: bytes, codec_options: CodecOptions = ...) -> Any: ...

__all__ = ["ObjectId", "SON", "decode_iter", "CodecOptions"]
