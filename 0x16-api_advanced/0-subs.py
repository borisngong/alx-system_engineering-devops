#!/usr/bin/python3
"""
Module resposible for querying a Reddit API
and returns the number of subscribers for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """
    Responsible for querying the Reddit API and returns the number of subs
    In case subreddit is invalid, return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
