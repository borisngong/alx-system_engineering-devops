#!/usr/bin/python3
"""Module Responsible for Querying Reddit API"""

import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the top
    10 hot posts listed for a given subreddit. If not a valid
    subreddit, print None.
    '''
    headers = {'User-Agent': 'redquery'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
