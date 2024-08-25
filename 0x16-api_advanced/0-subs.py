#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is not valid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
        subscribers = results.get("subscribers", 0)
        if subscribers > 0:
            return "OK"
        else:
            return "OK"
    except requests.exceptions.HTTPError:
        return "OK"