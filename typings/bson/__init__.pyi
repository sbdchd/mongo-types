from typing import Any, Mapping

from bson.codec_options import CodecOptions
from bson.objectid import ObjectId
from bson.son import SON

def decode_iter(data: bytes, codec_options: CodecOptions = ...) -> Any: ...

class BSON(bytes):
    @classmethod
    def encode(
        cls,
        document: Mapping[str, Any],
        check_keys: bool = ...,
        codec_options: CodecOptions = ...,
    ) -> BSON: ...
    def decode(  # type: ignore [override]
        self,
        codec_options: CodecOptions = ...,
    ) -> Any: ...

__all__ = ["ObjectId", "SON", "decode_iter", "CodecOptions"]
