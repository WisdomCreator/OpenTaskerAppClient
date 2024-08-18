from pywebio import *
from api import API

api = API('test', 'test')


def get_tasks():
    response = api.tasks.get()

    if response.code == 200:
        return response.body

    return []


def main():
    tasks = get_tasks()

    with output.use_scope('tasks'):
        table = [['Title', 'Description']]

        for task in tasks:
            table.append([task.title, task.description])

        output.put_text('Category')
        output.put_table(table)


start_server(main, port=8080, debug=True, auto_open_webbrowser=True)
