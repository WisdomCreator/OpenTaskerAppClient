from .models import Category
from .models import Response
from .api_base import APIBase


class Categories(APIBase):
    def create(self, title):
        category = Category(0, title)
        code = 201
        body = category

        response = Response(code, body)

        return response

    def get(self):
        category = Category(0, 'Hello, world!')
        code = 200
        body = [category,] * 3

        response = Response(code, body)

        return response

    def get_by_id(self, id):
        category = Category('Hello, world!', id)
        code = 200
        body = category

        response = Response(code, body)

        return response

    def update(self, id, title=None):
        code = 204

        response = Response(code)

        return response

    def delete(self, id):
        code = 204

        response = Response(code)

        return response

