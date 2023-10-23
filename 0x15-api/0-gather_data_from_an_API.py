#!/usr/bin/python3
"""Script using REST API for an employee ID"""

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

    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    tasks_done = []
    done = 0

    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in tasks_done:
        print("\t {}".format(task.get('title')))
