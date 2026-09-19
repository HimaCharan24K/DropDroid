
def add_to_queue(state, episode):

    state["queue"].append(
        episode
    )

    return state


def get_queue(state):

    return state["queue"]


def get_next_episode(state):

    if not state["queue"]:
        return None

    return state["queue"][0]


def remove_from_queue(state):

    if state["queue"]:
        state["queue"].pop(0)

    return state


def mark_completed(state, episode):

    state["completed"].append(
        episode
    )

    return state


def is_completed(state, video_id):

    for episode in state["completed"]:

        if episode["video_id"] == video_id:
            return True

    return False


if __name__ == "__main__":

    state = {
        "queue": [
            {
                "channel": "Lenny",
                "video_id": "A1",
                "title": "Episode 1"
            },
            {
                "channel": "Lex",
                "video_id": "B1",
                "title": "Episode 2"
            }
        ],
        "completed": []
    }

    episode = get_next_episode(state)

    mark_completed(
        state,
        episode
    )

    remove_from_queue(
        state
    )

    print()
    print("QUEUE:")
    print(get_queue(state))

    print()
    print("COMPLETED:")
    print(state["completed"])
