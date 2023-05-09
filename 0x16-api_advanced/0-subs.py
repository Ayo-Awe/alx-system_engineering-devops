#!/usr/bin/python3
"""This module contains code for querying
the reddit API total subscribers on a subreddit
"""
import requests

reddit_url = "https://www.reddit.com/r/{}/about.json"


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a
    given subreddit"""

    url = reddit_url.format(subreddit)
    response = requests.get(
        url, headers={"User-Agent": "hello mehowin my room"},
        allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data["data"]["subscribers"]
