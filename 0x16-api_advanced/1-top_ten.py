#!/usr/bin/python3
"""This module contains code for querying
the reddit API total subscribers on a subreddit
"""
import requests

reddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10"


def top_ten(subreddit):
    """Prints the titles of the top ten hot
    posts for a given subreddit
    """

    url = reddit_url.format(subreddit)
    response = requests.get(
        url, headers={"User-Agent": "hello mehowin my room"},
        allow_redirects=False)

    if response.status_code != 200:
        print(None)

    posts = response.json()["data"]["children"]

    for post in posts:
        print(post["data"]["title"])
