#!/usr/bin/python3
"""Module Responsible for Querying Reddit API"""

import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the top
    10 hot posts listed for a given subreddit. If not a valid
    subreddit, print None.
    '''
    reddit_app_info = {'User-Agent': 'my_reddit_app:v1.0.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=reddit_app_info,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
