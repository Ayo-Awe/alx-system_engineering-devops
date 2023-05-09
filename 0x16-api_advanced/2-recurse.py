#!/usr/bin/python3
"""This module contains code for querying
the reddit API total subscribers on a subreddit
"""
import requests

reddit_url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"


def recurse(subreddit, hot_list=[], after=""):
    """Return a list containing the titles of
    all hot posts for a given subreddit
    """
    if after is None:
        return hot_list

    url = reddit_url.format(subreddit, after)

    response = requests.get(
        url, headers={"User-Agent": "hello mehowin my room"},
        allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    after = data["data"]["after"]

    posts = map(lambda x: x["data"]["title"], data["data"]["children"])
    hot_list.extend(posts)

    return recurse(subreddit, hot_list, after)
