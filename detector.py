def is_new_video(latest_video_id, last_video_id):

    return latest_video_id != last_video_id


if __name__ == "__main__":

    print(
        is_new_video(
            "NEW123",
            "OLD456"
        )
    )

    print(
        is_new_video(
            "SAME123",
            "SAME123"
        )
    )
