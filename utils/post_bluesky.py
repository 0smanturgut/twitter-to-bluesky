from atproto import Client
import os

def post_to_bluesky(text, media_paths):
    try:
        client = Client()
        client.login(os.getenv("BLUESKY_USERNAME"), os.getenv("BLUESKY_APP_PASSWORD"))
        if media_paths:
            print("Post medya ile gönderiliyor...")
            client.send_post(text, media_paths)
        else:
            print("Post sadece metinle gönderiliyor...")
            client.send_post(text)
        print("Post başarıyla gönderildi.")
    except Exception as e:
        print(f"Post gönderme hatası: {e}")
