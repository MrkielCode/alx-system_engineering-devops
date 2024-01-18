#!/usr/bin/python3
"""
getting the total numbers of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    # getting url from reddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # getting the response
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        subscribers = json_response['data']['subscribers']
        return subscribers
    else:
        return 0
