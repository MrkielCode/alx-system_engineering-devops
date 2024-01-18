#!/usr/bin/python3
"""
getting the total numbers of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ getting number of subscribers """

    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        subscribers = json_response['data']['subscribers']
        return subscribers
    else:
        return 0
