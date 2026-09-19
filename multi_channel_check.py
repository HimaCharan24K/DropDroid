
from state import load_state, save_state
from channel_manager import load_channels
from youtube_service import get_latest_video
from detector import is_new_video
from queue_manager import add_to_queue


def check_all_channels():

    state = load_state()

    for channel in load_channels():

        handle = channel["youtube_handle"]

        url = f"https://www.youtube.com/{handle}/videos"

        latest = get_latest_video(url)

        latest_video_id = latest["video_id"]

        stored_video_id = (
            state["channels"]
            .get(handle, {})
            .get("last_video_id", "")
        )

        if is_new_video(
            latest_video_id,
            stored_video_id
        ):

            print()
            print("NEW VIDEO")
            print(channel["name"])
            print(latest["title"])

            episode = {
                "channel": channel["name"],
                "video_id": latest_video_id,
                "title": latest["title"],
		"url": latest["url"]
            }

            add_to_queue(
                state,
                episode
            )

            state["channels"][handle] = {
                "last_video_id": latest_video_id
            }

        else:

            print()
            print("NO NEW VIDEO")
            print(channel["name"])

    save_state(state)


if __name__ == "__main__":
    check_all_channels()
