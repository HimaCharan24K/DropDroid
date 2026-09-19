from multi_channel_check import check_all_channels

from state import (
    load_state,
    save_state
)

from queue_manager import (
    get_next_episode,
    remove_from_queue,
    mark_completed,
    is_completed
)

from download_service import download_audio

from telegram_service import (
    send_message,
    send_audio,
    create_episode_message
)

from episode_namer import (
    generate_episode_filename
)


def run():

    print("STEP 1: Discovering episodes...")

    check_all_channels()

    state = load_state()

    episode = get_next_episode(
        state
    )

    if not episode:

        print()
        print("QUEUE EMPTY")
        return

    if is_completed(
        state,
        episode["video_id"]
    ):

        print()
        print("ALREADY COMPLETED")
        print(episode["title"])

        remove_from_queue(
            state
        )

        save_state(
            state
        )

        return

    print()
    print("STEP 2: Downloading")
    print(episode["title"])

    file_name = generate_episode_filename(
        state,
        episode["channel"]
    )

    file_path = download_audio(
        episode["url"],
        file_name
    )

    print()
    print("STEP 3: Telegram")

    message = create_episode_message(
        episode["channel"],
        episode["title"]
    )

    send_message(
        message
    )

    send_audio(
        file_path
    )

    mark_completed(
        state,
        episode
    )

    remove_from_queue(
        state
    )

    save_state(
        state
    )

    print()
    print("DONE")


if __name__ == "__main__":
    run()
