from channel_manager import load_channels


channels = load_channels()

for channel in channels:

    print("Channel:", channel["name"])

    print("Handle:", channel["youtube_handle"])

    print()
