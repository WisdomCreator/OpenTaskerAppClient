from .tasks import Tasks
from .categories import Categories


class API:
    def __init__(self, api_url, api_key):
        self.__tasks = Tasks(api_url, api_key)
        self.__categories = Categories(api_url, api_key)

    @property
    def tasks(self):
        return self.__tasks

    @property
    def categories(self):
        return self.__categories
