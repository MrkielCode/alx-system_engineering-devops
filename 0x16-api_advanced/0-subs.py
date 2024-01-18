#!/usr/bin/python3
"""
getting the total numbers of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ getting number of subscribers """

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    json_response = response.json()
    subscribers = json_response.get('data')
    return subscribers.get('subscribers')
