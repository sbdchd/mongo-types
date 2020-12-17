from bson.codec_options import CodecOptions
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference
from pymongo.write_concern import WriteConcern

class BaseObject:
    @property
    def codec_options(self) -> CodecOptions: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_preference(self) -> ReadPreference: ...
    @property
    def read_concern(self) -> ReadConcern: ...
