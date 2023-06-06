#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'countSubs/0.01 (by GamerG_K)'}
    request = requests.get(url, headers=header, allow_redirects='False')
    if request.status_code == 200:
        count = request.json().get("data")
        return count.get("subscribers")
    else:
        return 0
