#!/usr/bin/python3
"""
script to get the users data and print out
the completed task
"""
import json
import requests


def get_user():
    """Get the user data"""
    api_url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data


def export_to_json(data):
    """Exporting to JSON file"""
    filename = "todo_all_employees.json"

    tasks_dict = {}
    for item in data:
        user_id = item['id']
        username = item['username']
        api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(api_url)
        if response.status_code == 200:
            todos = response.json()
            tasks_list = []
            for todo in todos:
                task = {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username
                }
                tasks_list.append(task)
            tasks_dict[user_id] = tasks_list

    with open(filename, 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)


def todo_done():
    """Get the tasks done"""
    data = get_user()  # Fetch user data once
    export_to_json(data)


if __name__ == "__main__":
    todo_done()
