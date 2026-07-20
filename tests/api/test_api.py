"""API тесты для Fake Store API."""

import requests


class TestFakeStoreAPI:
    """Тесты для Fake Store API."""

    BASE_URL = "https://fakestoreapi.com"

    def test_get_all_products(self):
        """Тест 1: Получение списка всех продуктов."""
        response = requests.get(f"{self.BASE_URL}/products")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"

        products = response.json()
        assert isinstance(products, list), "Ответ должен быть списком"
        assert len(products) > 0, "Список продуктов не должен быть пустым"
        assert len(products) == 20, "Должно быть 20 продуктов"

    def test_get_product_by_id(self):
        """Тест 2: Получение продукта по ID."""
        product_id = 1
        response = requests.get(f"{self.BASE_URL}/products/{product_id}")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"

        product = response.json()
        assert product["id"] == product_id, f"ID должен быть {product_id}"
        assert "title" in product, "Должно быть поле 'title'"
        assert "price" in product, "Должно быть поле 'price'"
        assert "category" in product, "Должно быть поле 'category'"

    def test_get_all_categories(self):
        """Тест 3: Получение списка всех категорий."""
        response = requests.get(f"{self.BASE_URL}/products/categories")

        assert response.status_code == 200, f"Ошибка: {response.status_code}"

        categories = response.json()
        assert isinstance(categories, list), "Ответ должен быть списком"
        assert len(categories) > 0, "Должны быть категории"

        expected_categories = [
            "electronics",
            "jewelery",
            "men's clothing",
            "women's clothing"
        ]
        for category in expected_categories:
            assert category in categories, f"Категория '{category}' не найдена"

    def test_login_success(self):
        """Тест 4: Успешная аутентификация."""
        credentials = {
            "username": "johnd",
            "password": "m38rmF$"
        }

        response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json=credentials
        )

        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        token = response.json()
        assert "token" in token, "Должен быть получен токен"
        assert isinstance(token["token"], str), "Токен должен быть строкой"
        assert len(token["token"]) > 0, "Токен не должен быть пустым"

    def test_login_fail_wrong_password(self):
        """Тест 5: Вход с неверным паролем."""
        credentials = {
            "username": "johnd",
            "password": "wrongpassword"
        }

        response = requests.post(
            f"{self.BASE_URL}/auth/login",
            json=credentials
        )

        assert response.status_code == 401, f"Ожидался 401, получен {response.status_code}"