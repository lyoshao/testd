"""API тесты для JSONPlaceholder."""

import allure
import pytest
from api.api_client import APIClient


@allure.epic("Тестирование API")
@allure.feature("Проверка данных")
class TestJSONPlaceholderAPI:
    """Тесты для JSONPlaceholder API."""

    @allure.story("Получение постов")
    def test_get_all_posts(self):
        """Тест 1: Получение списка всех постов."""
        client = APIClient()
        response = client.get("posts")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        posts = response.json()
        assert isinstance(posts, list), "Ответ должен быть списком"
        assert len(posts) > 0, "Список постов не должен быть пустым"
        assert len(posts) == 100, "Должно быть 100 постов"

    @allure.story("Получение поста по ID")
    def test_get_post_by_id(self):
        """Тест 2: Получение поста по ID."""
        client = APIClient()
        response = client.get("posts/1")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        post = response.json()
        assert post["id"] == 1, "ID должен быть 1"
        assert "title" in post, "Должно быть поле 'title'"
        assert "body" in post, "Должно быть поле 'body'"
        assert "userId" in post, "Должно быть поле 'userId'"

    @allure.story("Получение пользователей")
    def test_get_all_users(self):
        """Тест 3: Получение списка всех пользователей."""
        client = APIClient()
        response = client.get("users")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        users = response.json()
        assert isinstance(users, list), "Ответ должен быть списком"
        assert len(users) > 0, "Список пользователей не должен быть пустым"
        assert len(users) == 10, "Должно быть 10 пользователей"

    @allure.story("Создание поста")
    def test_create_post(self):
        """Тест 4: Создание нового поста."""
        client = APIClient()
        new_post = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        response = client.post("posts", json=new_post)

        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        post = response.json()
        assert "id" in post, "Должен быть получен ID"
        assert post["title"] == new_post["title"], "Название не совпадает"
        assert post["body"] == new_post["body"], "Тело не совпадает"

    @allure.story("Получение комментариев")
    def test_get_comments(self):
        """Тест 5: Получение комментариев к посту."""
        client = APIClient()
        response = client.get("posts/1/comments")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        comments = response.json()
        assert isinstance(comments, list), "Ответ должен быть списком"
        assert len(comments) > 0, "Должны быть комментарии"
        assert "postId" in comments[0], "Должно быть поле 'postId'"
        assert "name" in comments[0], "Должно быть поле 'name'"
        assert "email" in comments[0], "Должно быть поле 'email'"
        assert "body" in comments[0], "Должно быть поле 'body'"
