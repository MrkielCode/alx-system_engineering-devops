#!/usr/bin/python3
"""
script to get the users data and print out
the completed task
"""
import requests
from sys import argv


def get_user(id):
    """ get the user data"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data


def todo_done():
    """get the task done """
    id = argv[1]
    username = get_user(id).get('name')
    user_id = get_user(id).get('id')

    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(api_url)
    if response.status_code == 200:
        todo = response.json()
        total_task = len(todo)
    completed_todo = [task for task in todo if task.get('completed')]
    completed = len(completed_todo)

    print("Employee {} is done with tasks({}/{}):".format(
        username, completed, total_task))
    for todo in completed_todo:
        print('\t', todo['title'])


if __name__ == "__main__":
    todo_done()
