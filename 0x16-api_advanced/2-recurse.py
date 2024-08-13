#!/usr/bin/python3


"""Module responsible for querrying reddit API recursively"""


import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, the function returns None.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return None

    hot = response.json()['data']['children']
    aft = response.json()['data']['after']

    for post in hot:
        hot_list.append(post['data']['title'])

    if aft:
        recurse(subreddit, hot_list, aft)
    else:
        return hot_list
