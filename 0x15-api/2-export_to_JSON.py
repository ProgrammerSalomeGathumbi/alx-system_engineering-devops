#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    _id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(_id)).json()
    todos = requests.get(url + "todos", params={"userId": _id}).json()

    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump({_id: [{
                  "task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": user.get("username")}
                  for task in todos]}, jsonfile)
