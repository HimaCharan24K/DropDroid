
from yt_dlp import YoutubeDL
import os
import subprocess


def download_audio(url, output_file):

    before = set(os.listdir("downloads"))

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    print()
    print("DOWNLOADING...")
    print()

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    after = set(os.listdir("downloads"))

    new_files = after - before

    mp3_file = None

    for file in new_files:
        if file.endswith(".mp3"):
            mp3_file = f"downloads/{file}"
            break

    if not mp3_file:
        raise Exception("MP3 file not found")

    print()
    print("COMPRESSING...")
    print(mp3_file)

    compressed_file = output_file

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            mp3_file,
            "-ac",
            "1",
            "-b:a",
            "48k",
            compressed_file,
            "-y",
        ]
    )

    # remove original large mp3
    if os.path.exists(mp3_file):
        os.remove(mp3_file)

    print()
    print("COMPRESSED:")
    print(compressed_file)

    return compressed_file
