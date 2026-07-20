"""Клиент для API запросов."""

from typing import Optional, Dict, Any
import requests


class APIClient:
    """Базовый клиент для API."""

    BASE_URL = "https://fakestoreapi.com"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None):
        """GET запрос."""
        return requests.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            headers=self.HEADERS
        )

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None):
        """POST запрос."""
        return requests.post(
            f"{self.BASE_URL}/{endpoint}",
            json=json,
            headers=self.HEADERS
        )