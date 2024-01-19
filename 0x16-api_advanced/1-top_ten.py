#!/usr/bin/python3
"""
get the first ten host post of a given subreddict
"""
import requests


def top_ten(subreddit):
    """ Getting the top host post from subreddits"""
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
