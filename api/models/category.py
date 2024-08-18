
class Category:
    def __init__(self, title, id=None):
        self.__id = id
        self.__title = title

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title
