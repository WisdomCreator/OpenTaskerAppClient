
class Task:
    def __init__(self, title, description, category_id, id=None):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__category_id = category_id

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def category_id(self):
        return self.__category_id
