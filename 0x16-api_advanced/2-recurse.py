#!/usr/bin/python3
"""
Module to query the Reddit API and return a list of titles of all hot articles
for a given subreddit. If no results are found, return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Responsible for querying the Reddit API and returns a list of titles of
    all hot articles for a given subreddit

    Args:
        subreddit (str): represents subreddit to query.
        hot_list (list): represents List to store the titles of hot articles
        after (str): Represents The `after` parameter for pagination.

    Return:
            A list of titles, or None if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI/0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False
                            )

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for post in children:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
