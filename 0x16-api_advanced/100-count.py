#!/usr/bin/python3
"""
Module responsible for to query the Reddit API, parse the title of
all hot articles and print a sorted count of given keywords
"""

import requests
import sys
from collections import Counter


def count_words(subreddit, word_list, after='', counts=None):
    """
    Responsible for querying the Reddit API, parses the title of all hot
    articles and prints a sorted counts

    Args:
        subreddit (str): Represents subreddit to query.
        word_list (list): Respresents keywords to count in the titles
        after (str): Represents parameter for pagination.
        counts (Counter): Represents the Counter object

    """
    if counts is None:
        counts = Counter()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI/0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        json_children = json_data['data']['children']
        for post in json_children:
            title = post['data']['title'].lower().split()
            for word in word_list:
                counts[word.lower()] += title.count(word.lower())

        after = json_data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            categorized_counts = sorted(counts.items(),
                                        key=lambda x: (-x[1], x[0]))
            for word, count in categorized_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return
    else:
        return
