import os
import requests


BOT_TOKEN = os.getenv("DROP_DROID_BOT_TOKEN")
CHAT_ID = os.getenv("DROP_DROID_CHAT_ID")


def create_episode_message(channel, title):

    return f"""
🎙 {channel}

{title}

🎧 Audio attached
"""


def send_message(text):

    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Telegram is not configured")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def send_audio(file_path):

    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Telegram is not configured")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    with open(file_path, "rb") as audio:

        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID
            },
            files={
                "document": audio
            },
            timeout=300
        )

    response.raise_for_status()

    return response.json()
