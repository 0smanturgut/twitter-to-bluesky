from atproto import Client
import os

def post_to_bluesky(text, media_paths):
    client = Client()
    client.login(os.getenv("BLUESKY_USERNAME"), os.getenv("BLUESKY_APP_PASSWORD"))
    if media_paths:
        client.send_post(text, media_paths)
    else:
        client.send_post(text)
#
//  post_bluesky.py
//  
//
//  Created by Osman Turgut on 16/05/2025.
//

