#!/usr/bin/python3
"""request"""
import requests
import json
import csv


url = "https://jsonplaceholder.typicode.com/"
response = requests.get(url)


def fetch_and_print_posts(response):

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Tile: {post['title']}")


def fetch_and_save_posts(response):

    posts = response.json()
    for post in posts:
        if response.status_code == 200:
            list_dict = [{"id": post["id"], "title": post["title"],
                          "body": post["body"]}]
            with open("posts.csv", "w", newline='') as file:
                writer = csv.DictWriter(file,
                                        fieldnames=["id", "title", "body"])

                write.writeheader()
                writer.writerows(list_dict)
