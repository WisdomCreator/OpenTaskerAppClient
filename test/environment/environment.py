
class Environment:
    def __init__(self, api_url, api_key):
        self.__api_url = api_url
        self.__api_key = api_key
        self.__task_id = 0
        self.__task_title = 'TestTaskTitle'
        self.__task_description = 'TestTaskDescription'
        self.__task_category_id = 0
        self.__category_id = 0
        self.__category_title = 'TestCategoryTitle'

    @property
    def api_url(self):
        return self.__api_url

    @property
    def api_key(self):
        return self.__api_key

    @property
    def task_id(self):
        return self.__task_id

    @property
    def task_title(self):
        return self.__task_title

    @property
    def task_description(self):
        return self.__task_description

    @property
    def task_category_id(self):
        return self.__task_category_id

    @property
    def category_id(self):
        return self.__category_id

    @property
    def category_title(self):
        return self.__category_title
