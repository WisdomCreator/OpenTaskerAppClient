from .models import Task
from .models import Response
from .api_base import APIBase


class Tasks(APIBase):
    def create(self, category_id, title, description):
        task = Task(title, description, category_id, 0)
        code = 201
        body = task

        response = Response(code, body)

        return response

    def get(self):
        task = Task('Hello, world!', 'test description', 0, 0)
        code = 200
        body = [task,] * 3

        response = Response(code, body)

        return response

    def get_by_id(self, id):
        task = Task('Hello, world!', 'test description', 0, id)
        code = 200
        body = task

        response = Response(code, body)

        return response

    def update(self, id, category_id, title=None, description=None):
        code = 204

        response = Response(code)

        return response

    def delete(self, id):
        code = 204

        response = Response(code)

        return response
