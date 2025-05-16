from utils.fetch_tweets import get_latest_tweets
from utils.download_media import download_media
from utils.post_bluesky import post_to_bluesky
import os

def main():
    tweets = get_latest_tweets("ulanburki")
    print(f"{len(tweets)} tweet bulundu.")
    for tweet in tweets:
        print(f"Tweet: {tweet['content'][:80]}...")
        media_paths = download_media(tweet)
        print(f"Medya dosyaları: {media_paths}")
        post_to_bluesky(tweet['content'], media_paths)

main()  # Sadece bir kez hemen çalışsın diye
