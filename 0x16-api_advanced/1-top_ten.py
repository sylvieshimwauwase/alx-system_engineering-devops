#!/usr/bin/python3
"""printing titles of the 10 hot posts"""

from requests import get


def top_ten(subreddit):
    """the 10 hot posts"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    response = get(url, headers=headers, params=params)
    results = response.json()

    try:
        myData = results.get('data').get('children')

        for a in myData:
            print(a.get('data').get('title'))

    except Exception:
        print("None")
