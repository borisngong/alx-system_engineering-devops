#!/usr/bin/python3
"""Module Responsible for Querying Reddit API Recursively"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Responsible for returning all hot posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    users = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by boro)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=users, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
