from state import load_state
from queue_manager import get_next_episode
from download_service import download_audio


state = load_state()

episode = get_next_episode(state)

if episode:

    print("DOWNLOADING:")
    print(episode["title"])

    download_audio(
        episode["url"]
    )

else:

    print("QUEUE EMPTY")
