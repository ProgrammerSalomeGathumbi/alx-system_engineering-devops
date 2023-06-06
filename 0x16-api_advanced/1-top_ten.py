#!/usr/bin/python3
"""
queries Reddit API and prints  titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    prints titles of first 10 hot posts for a given subreddit
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'countSubs/0.01 (by GamerG_K)'}
    limit = {'limit': 10}
    request = requests.get(url, headers=header, params=limit,
                           allow_redirects=False)
    if request.status_code == 200:
        data = request.json()
        posts = data.get('data').get('children')
        for post in posts:
            title = post.get('data').get('title')
            print(title)
    else:
        print("None")
