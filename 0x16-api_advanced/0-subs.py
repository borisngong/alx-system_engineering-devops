#!/usr/bin/python3
"""
Responsible for querying a Reddit API and returns the number
of subscribers for a given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Responsible for querying the Reddit API and returns
    the number of subscribers.
    In case the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:reddit_subscriber_counter:v1.0.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        json_data = response.json()
        return json_data['data']['subscribers']
    except requests.exceptions.HTTPError:
        return 0
    except (KeyError, ValueError):
        return 0

