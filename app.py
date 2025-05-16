from utils.fetch_tweets import get_latest_tweets
from utils.download_media import download_media
from utils.post_bluesky import post_to_bluesky
import os

def main():
    tweets = get_latest_tweets("ulanburki")
    for tweet in tweets:
        media_paths = download_media(tweet)
        post_to_bluesky(tweet['content'], media_paths)

if __name__ == "__main__":
    main()
#
//  app.py
//  
//
//  Created by Osman Turgut on 16/05/2025.
//

