#!/usr/bin/python3
"""Exporting information of employees using JSON format"""


import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
                {
                    p.get("id"): [
                        {
                            "task": q.get("title"),
                            "completed": q.get("completed"),
                            "username": p.get("username")
                        }
                        for q in requests.get(
                            url + "todos",
                            params={"userId": p.get("id")}
                        ).json()
                    ]
                    for p in users
                },
                jsonfile
            )
