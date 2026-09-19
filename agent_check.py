from state import load_state, save_state
from youtube_service import get_latest_video
from detector import is_new_video


def check_channel():

    state = load_state()

    latest = get_latest_video(
        "https://www.youtube.com/@LennysPodcast/videos"
    )

    latest_video_id = latest["video_id"]

    last_video_id = state.get(
        "last_video_id",
        ""
    )

    if is_new_video(
        latest_video_id,
        last_video_id
    ):

        print("🎉 NEW VIDEO FOUND")

        print(
            latest["title"]
        )

        state["last_video_id"] = (
            latest_video_id
        )

        save_state(state)

    else:

        print(
            "✅ NO NEW VIDEO"
        )


if __name__ == "__main__":

    check_channel()
