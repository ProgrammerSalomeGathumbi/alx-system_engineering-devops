#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    list containing the titles of all hot articles
    in the subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'topTen/0.0.1(by /u/GamerG_K)'}
    request = requests.get(url, headers=header, allow_redirects=False)
    try:
        posts = request.json().get("data").get("children")

        if request.status_code == 200:
            for post in posts:
                title = post.get('data').get('title')
                hot_list.append(title)
        after = posts.get('data').get('after')
        count += len(posts)
        if after is not None:
            return recurse(subreddit, hot_list=hot_list, after=after,
                           count=count)
        else:
            return hot_list
    except Exception:
        print(None)
