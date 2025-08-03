#!/usr/bin/python3
"""csv"""
import csv
import json


def convert_csv_to_json(filename):
    """function to convert csv to json"""
    try:
        with open(filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file)
        return True
    except FileNotFoundError:
        return False
