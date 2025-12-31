import yt_dlp
import os

DONWLOAD_DIR ="download"
os.makedirs(DONWLOAD_DIR, exist_ok=True)

def exctratFormat(url:str):
    with yt_dlp.YoutubeDL({"quite":True}) as ydl:
        info = ydl.extract_info(url,download=False)
    
    formats = []
    for f in info["formats"]:
        if f.get("vcodec") != "none":
            formats.append({
                "format_id":f["format_id"],"resolution":f.get("resolution"),"ext":f.get('ext'),"fps":f.get("fps"),"filesize":f.get("filesize")
            })
    return formats


def downloadVideo(url:str,format_id:str):
    ydl_opts={
        "format":format_id,"outtmpl":f"{DONWLOAD_DIR}/%{title}s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
def downloadAudio(url:str, codec:str):
    ydl_opts = {
        "format" : "bestaudio/best",
        "outtmpl":f"{DONWLOAD_DIR}/%{title}s.%(ext)s",
        "postprocessor":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":codec,
            "preferredquality":192, 
        }]
    }

    with yt_dlp.YoutubeDL(yt_dlp) as ydl:
        ydl.download([url])