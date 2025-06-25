#!/usr/bin/python3
"""request"""
import requests
import json
import csv


def fetch_and_print_posts():
    """print post"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Tile: {post['title']}")
    else:
        print(f"Error fetching data")


def fetch_and_save_posts():
    """save posts"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

        list_dict = [{"id": post["id"], "title": post["title"],
                      "body": post["body"]}]
        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=["id", "title", "body"])
            write.writeheader()

            for post in posts:
                writer.writerows(list_dict)

        print("Data successfully saved to posts.csv")
    else:
        print("Error fetching data")
