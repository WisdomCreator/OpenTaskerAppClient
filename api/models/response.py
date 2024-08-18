
class Response:
    def __init__(self, code, body=None):
        self.__code = code
        self.__body = body

    @property
    def code(self):
        return self.__code

    @property
    def body(self):
        return self.__body
