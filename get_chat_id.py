import os
import requests


BOT_TOKEN = os.getenv("DROP_DROID_BOT_TOKEN")


if not BOT_TOKEN:
    raise RuntimeError("DROP_DROID_BOT_TOKEN is not configured")


url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

print(response.json())
