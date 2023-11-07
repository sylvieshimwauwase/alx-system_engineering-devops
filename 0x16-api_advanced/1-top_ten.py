#!/usr/bin/python3
"""printing titles of the 10 hot posts"""

import requests

def top_ten(subreddit):
    """the 10 hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            print("No posts found in this subreddit.")
        else:
            for post in posts:
                title = post['data']['title']
                print(title)

    else:
        print(f"Error: {response.status_code}. Subreddit may not exist.")
