# # Goal 🤝
# collect all of the links to the co-star images on instagram 

# Import libraries
from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api_extensions import pagination
from dotenv import load_dotenv
import os
import json

# load credintials from .env file
load_dotenv()
username = os.getenv('username')
password = os.getenv('password')


# login to instagram
api = Client(username = username, password = password)

# Inspect saved 
feed = api.saved_feed()['items']
feed

def get_link(feed):
    # Get the username and picture link
    user = feed['media']['user']['username']
    media_type = feed['media']['media_type']
    mapping = {1: 'Photo', 2: 'video', 8: 'swipe'}
    if media_type == 1:
        post = feed['media']['image_versions2']['candidates'][1]['url']
    else: post = None

    return (user, post)


# Get all saved posts
items = []
for results in pagination.page(api.saved_feed, args={}, wait = 3):
    
    # if data gets returned from the call
    if results.get('items'):

        feed = results.get('items')
        for item in feed:
            # get the username and link
            user, post = get_link(item)
            
            if user == 'costarastrology':
                items.append(post)
    
    print(f"Collected {len(items)} posts")



with open('image_links.json', 'w') as file:
    json.dump(items, file)






