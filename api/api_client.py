"""Клиент для API запросов."""

import requests


class APIClient:
    """Базовый клиент для API."""

    BASE_URL = "https://fakestoreapi.com"
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json"
    }

    def get(self, endpoint, params=None):
        """GET запрос."""
        return requests.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            headers=self.HEADERS,
            timeout=30
        )

    def post(self, endpoint, json=None):
        """POST запрос."""
        return requests.post(
            f"{self.BASE_URL}/{endpoint}",
            json=json,
            headers=self.HEADERS,
            timeout=30
        )