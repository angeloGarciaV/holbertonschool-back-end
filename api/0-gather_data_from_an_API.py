#!/usr/bin/python3
"""Module to gather data from an API"""
import requests
from sys import argv

user_id = argv[1]
EMPLOYEE_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/users?Id={user_id}').json()

todo_DATA = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
EMPLOYEE_NAME = EMPLOYEE_DATA[int(user_id)-1]["name"]

for tasks in todo_DATA:
    if tasks["completed"]:
        NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS += 1


print(
    'Employee {} is done with tasks({}/{})'
    .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
for tasks in todo_DATA:
    if tasks['completed']:
        print(f'\t{tasks['title']}')

if __name__ == "__main__":
    pass
