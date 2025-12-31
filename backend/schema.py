from pydantic import BaseModel
from typing import List,Optional

class VideoRequest(BaseModel):
    url:str

class FormatRespose(BaseModel):
    format_id : str
    resolution: Optional[str]
    ext:str
    fps:Optional[int]
    filesize:Optional[int]

class DownloadRequest(BaseModel):
    url:str
    format_id:str


class AudioRequest(BaseModel):
    url:str
    codec:str