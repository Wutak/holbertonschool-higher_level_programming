#!/usr/bin/python3
"""request"""
import requests
import csv


def fetch_and_print_posts():
    """request"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")
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

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]})

        print("Data successfully saved to posts.csv")
    else:
        print("Error fetching data")
