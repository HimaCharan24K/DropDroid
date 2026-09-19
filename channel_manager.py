import json


def load_channels():

    with open("channels.json", "r") as file:
        data = json.load(file)

    return data["channels"]


if __name__ == "__main__":

    channels = load_channels()

    for channel in channels:
        print(channel["name"])
        print(channel["youtube_handle"])
        print("-" * 30)
