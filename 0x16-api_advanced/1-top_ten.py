#!/usr/bin/python3
"""
Module responsible for quryin the REDDIT API top ten post listed
for a given subreddit
In case sureddit is invalid, return 0
"""


import requests


def top_ten(subreddit):
    """
    Functiom responsible for querying top ten post listed for a
    given sub reddit

    Return:
        if subreddit is invalid, return None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-agent': 'MyAPI/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        for posts in json_data['data']['children']:
            print(posts['data']['title'])
    else:
        print(None)
