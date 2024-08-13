#!/usr/bin/python3
"""Module for counting words in Reddit API"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0.1.0 (by /u/itsyaboijeff1000)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if f" {word} " in f" {title} ":
                word_count[word] = word_count.get(word, 0) + title.count(word)

    after = data.get("after")

    if after is None:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, after, word_count)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
