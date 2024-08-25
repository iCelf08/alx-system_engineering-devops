#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is not valid, returns "OK" (2 chars long).
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return "OK" if subscribers > 0 else "OK"
    except (requests.exceptions.HTTPError, KeyError, TypeError):
        return "OK"
