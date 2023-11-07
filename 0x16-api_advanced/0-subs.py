#!/usr/bin/python3
"""Function that returns number of subscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """returning number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

    response = get(url, headers=headers)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
