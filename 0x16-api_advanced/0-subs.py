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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    j_response = requests.get(url, headers=headers, allow_redirects=False)

    if j_response.status_code == 200:
        json_data = j_response.json()
        return json_data['data']['subscribers']
    else:
        return 0
