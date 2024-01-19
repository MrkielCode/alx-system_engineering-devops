#!/usr/bin/python3
"""
get the first ten host post of a given subreddict
"""
import requests


def top_ten(subreddit):
    """ Getting the top host post from subreddits"""
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
