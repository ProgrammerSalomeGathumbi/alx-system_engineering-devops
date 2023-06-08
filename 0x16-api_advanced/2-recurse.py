#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns the titles of all hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'topTen/0.0.1(by /u/GamerG_K)'}
    params = {'after': after}
    request = requests.get(url, headers=header, params=params,
                           allow_redirects=False)
    if request.status_code == 200:
        after = request.json().get('data').get('after')
        posts = request.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
