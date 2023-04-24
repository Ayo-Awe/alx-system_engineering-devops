#!/usr/bin/python3
"""This is a python script to fetch data from
an API and display the data formatted. This
script takes in exactly one argument, which is the
id of the user to be fetched
"""
import sys
import requests


def fetch_todos():
    """ Fetch todos for the specified employee,
    from the jsonplaceholder API
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user = requests.get(url).json()
    todos = requests.get(url + "/todos").json()
    return {"user": user, "todos": todos}


def format_todos(user_data):
    """Format the data fetched from the JSON placeholder
    API
    """
    todos = user_data.get("todos")
    user = user_data.get("user")
    total_tasks = len(todos)
    tasks_completed = list(filter(lambda x: x.get(
        "completed") is True, todos))

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(tasks_completed), total_tasks))

    for task in tasks_completed:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    user_data = fetch_todos()
    format_todos(user_data)
