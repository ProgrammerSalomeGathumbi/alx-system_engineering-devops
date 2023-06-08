#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    First 10 hot posts in the subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'topTen/0.0.1(by /u/GamerG_K)'}
    request = requests.get(url, headers=header, allow_redirects=False)
    try:
        posts = request.json().get("data").get("children")

        if request.status_code == 200:
            for post in posts[:10]:
                print(post.get('data').get('title'))
    except Exception:
        print(None)
