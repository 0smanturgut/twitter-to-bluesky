import yt_dlp
import os

def download_media(tweet):
    media_paths = []
    ydl_opts = {
        'outtmpl': 'media/%(id)s.%(ext)s',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(tweet['url'], download=True)
            media_paths.append(ydl.prepare_filename(info))
        except Exception as e:
            print(f"Media download failed: {e}")
    return media_paths
