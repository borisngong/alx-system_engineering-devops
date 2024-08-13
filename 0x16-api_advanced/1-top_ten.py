#!/usr/bin/python3
"""Module Responsible for Querying Reddit API"""

import requests


def top_ten(subreddit):
    '''
    Responsible for querying the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit,
    if no subreddit print None
    '''
    reddit_app_info = {'User-Agent': 'Boro'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=reddit_app_info,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
