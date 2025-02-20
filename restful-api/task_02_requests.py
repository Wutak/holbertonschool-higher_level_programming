#!/usr/bin/python3
"""request"""
import requests
import csv


def fetch_and_print_posts():
    """request"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:" response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        else:
            print("Error fecthing data")


def fetch_and_save_posts():
    """request"""

    response = resquests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        data = [{"id": post["id"], "title": post["title"],
                "body": post["body"]} for post in posts]
        with open("post.cv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data successfully written to posts.csv")
    else:
        print("Error fetching data")
