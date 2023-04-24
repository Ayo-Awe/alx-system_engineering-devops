#!/usr/bin/python3
"""This is a python script to fetch data from
an API and display the data formatted. This
script takes in exactly one argument, which is the
id of the user to be fetched. It exports the data
as a json file
"""
import json
import requests
import sys


def fetch_todos():
    """ Fetch todos for the specified employee,
    from the jsonplaceholder API
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    return {"user": user, "todos": todos}


def export_as_json(user_data):
    """Formats data fetched from the API and
    exports as a json file
    """
    employee_id = sys.argv[1]
    todos = user_data.get("todos")
    user = user_data.get("user")
    tasks = list(map(lambda x: {"username": user.get(
        "username"), "task": x.get("title"), "completed": x.get("completed")}, todos))

    with open("{}.json".format(employee_id), mode="w", newline="") as json_file:
        payload = {user.get("id"): tasks}
        json.dump(payload, json_file)


if __name__ == "__main__":
    user_data = fetch_todos()
    export_as_json(user_data)
