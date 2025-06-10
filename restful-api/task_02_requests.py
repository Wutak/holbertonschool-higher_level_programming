#!/usr/bin/python3
"""request"""
import requests


url = "https://jsonplaceholder.typicode.com/"
response = requests.get(url)

def fetch_and_print_posts(response):

    print("Status Code = 200")
    if response.status_code == 200:
        posts = response.json()
    for post in posts:
        print(f"Tile: {post['title']}")

def fetch_and_save_posts(response):

    for post in posts:
        if response.status_code == 200:

