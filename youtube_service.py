from yt_dlp import YoutubeDL


def get_latest_video(channel_url):

    ydl_opts = {
        "extract_flat": True,
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            channel_url,
            download=False
        )

        latest = info["entries"][0]

        return {
            "title": latest.get("title"),
            "video_id": latest.get("id"),
            "url": f"https://youtube.com/watch?v={latest.get('id')}"
        }


if __name__ == "__main__":

    video = get_latest_video(
        "https://www.youtube.com/@LennysPodcast/videos"
    )

    print(video)
