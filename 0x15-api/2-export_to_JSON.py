#!/usr/bin/python3
"""
script to get the users data and print out
the completed task
"""
import csv
import json
import requests
from sys import argv


def get_user(id):
    """ get the user data"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data


def export_to_json(user_id, username, todo):
    """ exporting to json file """
    filename = f"{user_id}.json"

    tasks_list = []
    for item in todo:
        task_list = {
            "task": item["title"],
            "completed": item["completed"],
            "username": username
            }
        tasks_list.append(task_list)
    with open(filename, 'w') as jsonfile:
        json.dump({user_id: tasks_list}, jsonfile)


def todo_done():
    """get the task done """
    id = argv[1]
    username = get_user(id).get("username")
    user_id = get_user(id).get('id')

    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(api_url)
    if response.status_code == 200:
        todo = response.json()
    export_to_json(user_id, username, todo)
    print(username)


if __name__ == "__main__":
    todo_done()
