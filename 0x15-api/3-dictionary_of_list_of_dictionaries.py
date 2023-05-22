#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    users = {}
    userlist = {}
    for name in user:
        _id = name.get("id")
        users[_id] = []
        userlist[_id] = name.get("username")
    todos = requests.get(url + "todos").json()
    for task in todos:
        task_list = {}
        _id = task.get("userId")
        task_list["username"] = userlist.get(_id)
        task_list["tasks"] = task.get("title")
        task_list["completed"] = task.get("completed")
        users.get(_id).append(task_list)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(users, jsonfile)
