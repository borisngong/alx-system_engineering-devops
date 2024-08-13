#!/usr/bin/python3
"""Module Responsible for Querying Reddit API Recursively"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Responsible for returning all hot posts on a given subreddit

    Args:
        subreddit (str): The subreddit to fetch hot posts from
        hot_list (list): The list of hot post titles
        (default is an empty list)
        after (str): The after parameter for pagination
        (default is an empty string)
        count (int): The count of posts fetched so far (default is 0)

    Returns:
        list: A list of hot post titles
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by boro)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers,
                                params=parameters, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
