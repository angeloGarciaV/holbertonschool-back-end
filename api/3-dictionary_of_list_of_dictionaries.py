#!/usr/bin/python3
"""Module to create CSV"""
import json
import requests
from sys import argv


EMPLOYEE_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/users').json()

todo_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/todos').json()


EMPLOYEE_NAME = EMPLOYEE_DATA["name"]
USER_ID = EMPLOYEE_DATA[int(user_id)-1]['id']
USERNAME = EMPLOYEE_DATA[int(user_id)-1]['username']


with open('todo_all_employees.json', 'w') as jsonfile:
    for employees in range(1, len(EMPLOYEE_DATA)):
        USER_DATA = {USER_ID: []}

        for tasks in todo_DATA:
            task_data = {
                "task": tasks['title'],
                "completed": tasks['completed'],
                "username": USERNAME}
            USER_DATA[USER_ID].append(task_data)

    json.dump(USER_DATA, jsonfile)
