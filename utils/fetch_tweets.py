import subprocess
import json

def get_latest_tweets(username, limit=5):
    command = [
        'snscrape',
        '--jsonl',
        f'--max-results={limit}',
        f'twitter-user {username}'
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("snscrape komutu başarısız oldu:", e)
        return []

    tweets_raw = result.stdout.strip().split("\n")
    tweets = []

    for line in tweets_raw:
        if line.strip() == "":
            continue  # Boş satır varsa geç
        try:
            tweet_data = json.loads(line)
            tweets.append({
                'id': tweet_data['id'],
                'content': tweet_data['content'],
                'url': tweet_data['url']
            })
        except json.JSONDecodeError as e:
            print("Tweet verisi çözülemedi:", e)
            continue

    return tweets
