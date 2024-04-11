#!/usr/bin/python3
import requests

"""Module to query number of subscribers of a subreddit."""


def count_words(subreddit, word_list, word_count=None, after=None):
    """Function to query number of subscribers of a subreddit."""
    if word_count is None:
        word_count = {}

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()

    if response.status_code is not 200:
        return None

    after = response.json().get('data').get('after')

    if after is None:
        for i in response.json().get('data').get('children'):
            title = i.get('data').get('title')
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        if len(word_count) == 0:
            return

        for key, value in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(key, value))
        return

    for i in response.json().get('data').get('children'):
        title = i.get('data').get('title')
        for word in word_list:
            if word.lower() in title.lower():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return count_words(subreddit, word_list, word_count, after)
