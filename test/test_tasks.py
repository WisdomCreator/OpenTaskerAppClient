from api.tasks import Tasks


class TestTasks:
    @staticmethod
    def test_create(environment):
        tasks = Tasks(environment.api_url, environment.api_key)

        response = tasks.create(environment.category_id, environment.task_title, environment.task_description)

        assert response.code == 201

    @staticmethod
    def test_get(environment):
        tasks = Tasks(environment.api_url, environment.api_key)

        response = tasks.get()

        assert response.code == 200

    @staticmethod
    def test_get_by_id(environment):
        tasks = Tasks(environment.api_url, environment.api_key)

        response = tasks.get_by_id(environment.task_id)

        assert response.code == 200

    @staticmethod
    def test_update(environment):
        tasks = Tasks(environment.api_url, environment.api_key)

        response = tasks.update(environment.task_id, environment.category_id, environment.task_title,
                                environment.task_description)

        assert response.code == 204

    @staticmethod
    def test_delete(environment):
        tasks = Tasks(environment.api_url, environment.api_key)

        response = tasks.delete(environment.task_id)

        assert response.code == 204
