#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    returns the titles of all hot articles for a given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'tenPosts/0.01 (by GamerG_K)'}
    params = {'limit': 10, 'after': after, 'count': count}
    request = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
    if request.status_code == 200:
        posts = request.json().get('data').get('children')
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
    else:
        return None
