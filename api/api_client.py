"""Клиент для API запросов."""

import requests


class APIClient:
    """Базовый клиент для API."""

    BASE_URL = "https://fakestoreapi.com"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Referer": "https://fakestoreapi.com/"
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