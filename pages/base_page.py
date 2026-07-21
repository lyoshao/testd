"""Базовая страница с общими методами."""

import os
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class BasePage:
    """Базовый класс с общими методами для всех страниц."""

    def __init__(self, page: Page):
        self.page = page
        self.is_ci = os.environ.get("CI") == "true"
        self.timeout = 60000 if self.is_ci else 30000
        self.short_timeout = 15000 if self.is_ci else 10000

    def open(self, url: str) -> None:
        """Открывает URL и ждет загрузки страницы."""
        try:
            self.page.goto(url, timeout=self.timeout)
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_timeout(500 if self.is_ci else 1000)
        except PlaywrightTimeoutError as e:
            print(f"Таймаут при открытии {url}: {e}")
            raise
        except Exception as e:
            print(f"Ошибка при открытии {url}: {e}")
            raise

    def click_element(self, selector: str) -> None:
        """Кликает на элемент по селектору."""
        try:
            self.page.wait_for_selector(selector, timeout=self.short_timeout)
            self.page.click(selector)
        except PlaywrightTimeoutError:
            try:
                self.page.click(selector)
            except PlaywrightTimeoutError:
                print(f"Элемент не найден для клика: {selector}")
            except Exception as e:
                print(f"Ошибка при клике на {selector}: {e}")

    def fill_input(self, selector: str, text: str) -> None:
        """Заполняет поле ввода текстом."""
        try:
            self.page.wait_for_selector(selector, timeout=self.short_timeout)
            self.page.fill(selector, text)
        except PlaywrightTimeoutError:
            try:
                self.page.fill(selector, text)
            except PlaywrightTimeoutError:
                print(f"Поле ввода не найдено: {selector}")
            except Exception as e:
                print(f"Ошибка при заполнении поля {selector}: {e}")

    def get_text(self, selector: str) -> str:
        """Получает текст элемента, возвращает пустую строку если не найден."""
        try:
            element = self.page.locator(selector)
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except PlaywrightTimeoutError:
            return ""
        except Exception as e:
            print(f"Ошибка при получении текста с {selector}: {e}")
            return ""

    def is_element_visible(self, selector: str) -> bool:
        """Проверяет, видим ли элемент."""
        try:
            self.page.wait_for_selector(selector, timeout=self.short_timeout)
            return self.page.is_visible(selector)
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при проверке видимости {selector}: {e}")
            return False

    def wait_for_url_contains(self, text: str) -> None:
        """Ожидает, пока URL будет содержать заданный текст."""
        try:
            self.page.wait_for_url(f"**/{text}**", timeout=self.short_timeout)
        except PlaywrightTimeoutError:
            print(f"URL не содержит {text} за время ожидания")
        except Exception as e:
            print(f"Ошибка при ожидании URL: {e}")
