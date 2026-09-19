
import feedparser


def fetch_feed(feed_url):
    return feedparser.parse(feed_url)


def get_latest_episode(feed):

    if not feed.entries:
        return None

    return feed.entries[0]


feed_url = "https://feeds.megaphone.fm/lennyspodcast"

feed = feedparser.parse(feed_url)

print("Entries:", len(feed.entries))
print("Bozo:", feed.bozo)

if hasattr(feed, "status"):
    print("Status:", feed.status)

print(feed.keys())
