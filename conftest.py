"""Фикстуры для Playwright."""

import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """Создает новую страницу браузера для каждого теста."""
    with sync_playwright() as p:
        is_ci = os.environ.get("CI") == "true"
        browser = p.chromium.launch(
            headless=is_ci,
            slow_mo=0 if is_ci else 500
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()
        yield page
        browser.close()
