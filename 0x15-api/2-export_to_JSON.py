#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = []
    for task in todos:
        task_list = {}
        task_list["tasks"] = task.get("title")
        task_list["completed"] = task.get("completed")
        task_list["username"] = user.get("username")
        tasks.append(task_list)
    jsondict = {}
    jsondict[argv[1]] = tasks
    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump(jsondict, jsonfile)
