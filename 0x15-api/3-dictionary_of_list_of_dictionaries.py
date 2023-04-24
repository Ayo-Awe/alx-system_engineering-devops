#!/usr/bin/python3
"""This is a python script to fetch data from
an API and display the data formatted.
It fetches all employees and exports the data
as a json file.
"""
import json
import requests


def fetch_employes_and_todos():
    """ Fetch all employees and todos from
    the JSON placeholder API
    """
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    return {"users": users, "todos": todos}


def get_employee_todos(employee_id, todos):
    """Filters through a list of employee todos and returns
    a list of todos for this employee
    """

    return list(filter(lambda x: x.get("userId") == employee_id, todos))


def format_employee_todos(username, employee_todos):
    """Returns an array containing the todos for
    this employee in the following format

     [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
     "username": "USERNAME"}, {"task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}]
    """

    formatted_todos = list(map(lambda x: {"task": x.get("title"),
                                          "completed": x.get(
        "completed"), "username": username}, employee_todos))

    return formatted_todos


def export_as_json(employee_data):
    """Formats data fetched from the API and
    exports as a json file
    """
    payload = {}

    users = employee_data.get("users")
    todos = employee_data.get("todos")

    for user in users:
        user_todos = get_employee_todos(user.get("id"), todos)
        user_todos = format_employee_todos(user.get("username"), user_todos)
        payload[user.get("id")] = user_todos

    with open("todo_all_employees.json", mode="w",
              newline="")as json_file:
        json.dump(payload, json_file)


if __name__ == "__main__":
    employee_data = fetch_employes_and_todos()
    export_as_json(employee_data)
