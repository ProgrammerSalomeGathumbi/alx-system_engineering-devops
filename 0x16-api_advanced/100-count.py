#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after='', sorted_words={}):
    """
    prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
     Javascript should count as javascript, but java should not)
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
            title = post.get('data').get('title')
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if sorted_words.get(word) is None:
                        sorted_words[word] = times
                    else:
                        sorted_words[word] += times
        if after is None:
            if len(sorted_words) == 0:
                print("")
                return
            sorted_words = sorted(sorted_words.items(), key=lambda kv:
                                  (-kv[1], kv[0]))
            [print("{}: {}".format(k, v)) for k, v in sorted_words]
        else:
            return count_words(subreddit, word_list, after, sorted_words)
    else:
        return None
