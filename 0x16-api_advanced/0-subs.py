import requests

#!/usr/bin/python3
"""
Module to query number of subscribers of a subreddit
"""



def number_of_subscribers(subreddit):
    """
    Function to query number of subscribers of a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
