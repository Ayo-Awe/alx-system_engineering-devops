#!/usr/bin/python3
"""This is a python script to fetch data from
an API and display the data formatted. This
script takes in exactly one argument, which is the
id of the user to be fetched. It exports the data
as a csv
"""
import csv
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


def export_as_csv(user_data):
    """Formats data fetched from the API and
    exports as a csv
    """
    employee_id = sys.argv[1]
    with open("{}.csv".format(employee_id), mode="w", newline="") as csvFile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(
            csvFile, fieldnames=fieldnames, extrasaction="ignore",
            quoting=csv.QUOTE_ALL)

        todos = user_data.get("todos")
        username = user_data.get("user").get("username")
        for todo in todos:
            todo["username"] = username
            writer.writerow(todo)


if __name__ == "__main__":
    user_data = fetch_todos()
    export_as_csv(user_data)
