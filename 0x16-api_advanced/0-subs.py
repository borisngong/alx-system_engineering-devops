#!/usr/bin/python3
"""
Responsible for querying a Reddit API and returns the number of
subscribers for a given subreddit
"""


import requests


def number_of_subscribers(subreddit: str) -> int:
    """
    Responsible for querying the Reddit API and returns the
    number of subscribers
    In case subreddit is invalid, return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:reddit_subscriber_counter:v1.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    elif response.status_code == 200:
        json_data = response.json()
        return json_data['data']['subscribers']
    else:
        return 0

