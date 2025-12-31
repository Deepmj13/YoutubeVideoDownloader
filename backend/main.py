from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from schema import (
    VideoRequest,FormatRespose,DownloadRequest,AudioRequest
)

from downloader import(
    exctratFormat,downloadVideo,downloadAudio
)


app = FastAPI(
    title="Youtube media downloader api",
    description="Download YouTube videos and audio with quality selection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/formats",response_model=list[FormatRespose])
def getFormats(data:VideoRequest):
    try:
        return  exctratFormat(data.url)
    except Exception as e:
        raise HTTPException(status="400",details=str(e))

@app.post("/downlaod/video")
def downloadVideoAPI(data: VideoRequest):
    try:
        return downloadVideo(data.url, data.format_id)
    except Exception as e:
        return HTTPException(status="400",details=str(e))


@app.post("/download/audio")
def downloadAudioAPI(data:AudioRequest):
    try:
        return downloadAudio(data.url, data.format_id)
    except Exception as e:
        return HTTPException(status="400",details=str(e))
        
