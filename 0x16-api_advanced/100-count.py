#!/usr/bin/python3
""" Module Responsible for a function that queries the
Reddit API Recursively
"""


import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    A function responsible for querying the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """
    if word_dict is None:
        word_dict = {}
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

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
        title = post['data']['title']
        lower = [word.lower() for word in title.split(' ')]

        for word in word_dict.keys():
            word_dict[word] += lower.count(word)

    count_words(subreddit, word_list, aft, word_dict)
