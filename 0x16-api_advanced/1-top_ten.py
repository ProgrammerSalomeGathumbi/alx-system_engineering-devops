#!/usr/bin/python3
"""
queries Reddit API and prints  titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    prints titles of first 10 hot posts for a given subreddit
    """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'tenPosts/0.01 (by GamerG_K)'}
    params = {'limit': 10}
    request = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
    if request.status_code == 200:
        data = response.json().get("data")
        posts = data.get("data").get("children")
        for post in posts:
            title = post.get("data").get("title")
            print(title)
    else:
        print("None")
