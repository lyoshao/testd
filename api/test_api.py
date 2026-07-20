"""API тесты для Fake Store API."""

import allure
from api.api_client import APIClient


@allure.epic("Тестирование API")
class TestFakeStoreAPI:
    """Тесты для Fake Store API."""

    @allure.feature("Проверка продуктов")
    @allure.story("Получение всех продуктов")
    def test_get_all_products(self):
        """Тест 1: Получение списка всех продуктов."""
        client = APIClient()
        response = client.get("products")
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        products = response.json()
        assert isinstance(products, list), "Ответ должен быть списком"
        assert len(products) > 0, "Список продуктов не должен быть пустым"
        assert len(products) == 20, "Должно быть 20 продуктов"

    @allure.feature("Проверка продуктов")
    @allure.story("Получение продукта по ID")
    def test_get_product_by_id(self):
        """Тест 2: Получение продукта по ID."""
        client = APIClient()
        response = client.get("products/1")
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        product = response.json()
        assert product["id"] == 1, "ID должен быть 1"
        assert "title" in product, "Должно быть поле 'title'"
        assert "price" in product, "Должно быть поле 'price'"
        assert "category" in product, "Должно быть поле 'category'"

    @allure.feature("Проверка продуктов")
    @allure.story("Получение категорий")
    def test_get_all_categories(self):
        """Тест 3: Получение списка всех категорий."""
        client = APIClient()
        response = client.get("products/categories")
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        categories = response.json()
        assert isinstance(categories, list), "Ответ должен быть списком"
        assert len(categories) > 0, "Должны быть категории"
        expected_categories = ["electronics", "jewelery", "men's clothing", "women's clothing"]
        for category in expected_categories:
            assert category in categories, f"Категория '{category}' не найдена"

    @allure.feature("Авторизация")
    @allure.story("Успешная авторизация")
    def test_login_success(self):
        """Тест 4: Успешная аутентификация."""
        client = APIClient()
        credentials = {
            "username": "johnd",
            "password": "m38rmF$"
        }
        response = client.post("auth/login", json=credentials)
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        token = response.json()
        assert "token" in token, "Должен быть получен токен"
        assert isinstance(token["token"], str), "Токен должен быть строкой"
        assert len(token["token"]) > 0, "Токен не должен быть пустым"

    @allure.feature("Авторизация")
    @allure.story("Негативные сценарии")
    def test_login_fail_wrong_password(self):
        """Тест 5: Вход с неверным паролем."""
        client = APIClient()
        credentials = {
            "username": "johnd",
            "password": "wrongpassword"
        }
        response = client.post("auth/login", json=credentials)
        assert response.status_code == 401, f"Ожидался 401, получен {response.status_code}"
