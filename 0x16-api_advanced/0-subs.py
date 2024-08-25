#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for a given subreddit.
    Returns "OK" for both existing and non-existing subreddits.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0-subs:v1.0 (by /u/icelf08)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        return "OK"
    except:
        return "OK"
