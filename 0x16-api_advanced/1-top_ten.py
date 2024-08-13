#!/usr/bin/python3
"""Reddit API"""
import json
import requests

def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
