#!/usr/bin/python3
"""Function that returns number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """returning number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print(f"Error: {response.status_code}. Subreddit may not exist.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return 0
