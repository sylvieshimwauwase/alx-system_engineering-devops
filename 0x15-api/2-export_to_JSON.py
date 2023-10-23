#!/usr/bin/python3
"""Script using REST API for an employee ID"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    if response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })

    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)
