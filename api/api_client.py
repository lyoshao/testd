"""Клиент для API запросов."""

import requests


class APIClient:
    """Базовый клиент для API."""

    BASE_URL = "https://fakestoreapi.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        })

    def get(self, endpoint, params=None):
        """GET запрос."""
        return self.session.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            timeout=30
        )

    def post(self, endpoint, json=None):
        """POST запрос."""
        return self.session.post(
            f"{self.BASE_URL}/{endpoint}",
            json=json,
            timeout=30
        )