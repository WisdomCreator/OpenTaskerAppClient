from api.categories import Categories


class TestCategory:
    @staticmethod
    def test_create(environment):
        categories = Categories(environment.api_url, environment.api_key)

        response = categories.create(environment.task_title)

        assert response.code == 201

    @staticmethod
    def test_get(environment):
        categories = Categories(environment.api_url, environment.api_key)

        response = categories.get()

        assert response.code == 200

    @staticmethod
    def test_get_by_id(environment):
        categories = Categories(environment.api_url, environment.api_key)

        response = categories.get_by_id(environment.category_id)

        assert response.code == 200

    @staticmethod
    def test_update(environment):
        categories = Categories(environment.api_url, environment.api_key)

        response = categories.update(environment.category_id, environment.category_title)

        assert response.code == 204

    @staticmethod
    def test_delete(environment):
        categories = Categories(environment.api_url, environment.api_key)

        response = categories.delete(environment.category_id)

        assert response.code == 204
