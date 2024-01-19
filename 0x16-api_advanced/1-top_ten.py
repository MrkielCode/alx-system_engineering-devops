#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'your_user_agent'}  # Set a user agent to avoid 429 error (rate limiting)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return

    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])