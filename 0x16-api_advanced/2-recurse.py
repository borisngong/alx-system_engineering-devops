#!/usr/bin/python3
"""Module Responsible for Querying Reddit API"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {"User-Agent": "linux"}

    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=user, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json()

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    after = data["data"]["after"]
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
