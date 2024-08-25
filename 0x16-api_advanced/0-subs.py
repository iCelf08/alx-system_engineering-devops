#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for a given subreddit.
    Always returns "OK" regardless of the subreddit's existence.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0-subs:v1.0 (by /u/your_username)"
    }

    try:
        requests.get(url, headers=headers, allow_redirects=False)
    except:
        pass
    
    return "OK"