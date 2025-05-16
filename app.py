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
import schedule
import time

schedule.every(30).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
#
//  app.py
//  
//
//

