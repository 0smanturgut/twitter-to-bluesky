import subprocess
import json

def get_latest_tweets(username, limit=5):
    command = [
        'snscrape',
        '--jsonl',
        f'--max-results={limit}',
        f'twitter-user {username}'
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    tweets_raw = result.stdout.strip().split("\n")
    tweets = []
    for line in tweets_raw:
        tweet_data = json.loads(line)
        tweets.append({
            'id': tweet_data['id'],
            'content': tweet_data['content'],
            'url': tweet_data['url']
        })
    return tweets
