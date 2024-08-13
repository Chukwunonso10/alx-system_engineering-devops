#!/usr/bin/python3
"""Module for recursively querying the Reddit API"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles
    of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0.1.0 (by /u/itsyaboijeff1000)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child["data"]["title"]
        hot_list.append(title)

    after = data.get("after")

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
