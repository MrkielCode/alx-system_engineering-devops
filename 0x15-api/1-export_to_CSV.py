#!/usr/bin/python3
"""
script to get the users data and print out
the completed task
"""
import csv
import requests
from sys import argv


def get_user(id):
    """ get the user data"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data


def export_to_csv(user_id, username, todo):
    """ exporting to json file """
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            csv_writer.writerow([
                user_id, username,
                str(task['completed']),
                task['title']])


def todo_done():
    """get the task done """
    id = argv[1]
    username = get_user(id).get("username")
    user_id = get_user(id).get('id')

    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(api_url)
    if response.status_code == 200:
        todo = response.json()
    export_to_csv(user_id, username, todo)
    print(username)


if __name__ == "__main__":
    todo_done()
