
def generate_episode_filename(state, channel):

    count = 0

    for episode in state["completed"]:
        if episode["channel"] == channel:
            count += 1

    episode_number = count + 1

    safe_channel = (
        channel
        .replace("'", "")
        .replace("/", "-")
    )

    return f"downloads/{safe_channel}_->E{episode_number:03d}.mp3"
