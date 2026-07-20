"""Главная страница."""

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница Wildberries."""

    SEARCH_INPUT = "input#searchInput"
    CATALOG_BUTTON = "button[data-wba-header-name='Catalog']"
    CATALOG_CONTAINER = "div#menuBurger"
    CATEGORY_ITEM = "li.menu-burger__main-list-item a"
    SUBCATEGORY_PANEL = "div.menu-burger__first"

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.wildberries.by/"

    def open_main_page(self) -> None:
        """Открывает главную страницу."""
        self.open(self.url)

    def search_product(self, query: str) -> None:
        """Ищет товар по запросу."""
        self.fill_input(self.SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1500)
    
    def is_search_button_visible(self) -> bool:
        """Проверяет, видима ли кнопка поиска."""
        try:
            search_button = self.page.locator("button.search-catalog__btn--search")
            return search_button.count() > 0 and search_button.first.is_visible()
        except Exception:
            return False

    def clear_search_field(self) -> bool:
        """Очищает поле поиска через кнопку 'Очистить поиск'."""
        try:
            clear_button = self.page.locator("button.search-catalog__btn--clear")
            if clear_button.count() > 0 and clear_button.is_visible():
                clear_button.click()
                self.page.wait_for_timeout(500)
                return True
            return False
        except Exception:
            return False

    def open_catalog(self) -> bool:
        """Открывает панель каталога."""
        try:
            button = self.page.locator(self.CATALOG_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return self.is_catalog_panel_open()
            return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при открытии каталога: {e}")
            return False

    def is_catalog_panel_open(self) -> bool:
        """Проверяет, открыта ли панель каталога."""
        try:
            container = self.page.locator(self.CATALOG_CONTAINER)
            if container.count() > 0:
                class_attr = container.first.get_attribute("class") or ""
                return "active" in class_attr
            return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при проверке панели каталога: {e}")
            return False

    def close_catalog(self) -> bool:
        """Закрывает панель каталога."""
        try:
            button = self.page.locator(self.CATALOG_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при закрытии каталога: {e}")
            return False

    def get_catalog_categories(self) -> list:
        """Возвращает список категорий из панели каталога."""
        try:
            return self.page.locator(self.CATEGORY_ITEM).all()
        except Exception:
            return []

    def is_category_exists(self, category_name: str) -> bool:
        """Проверяет, существует ли категория в каталоге."""
        try:
            category = self.page.locator(
                f"{self.CATEGORY_ITEM}:has-text('{category_name}')"
            )
            return category.count() > 0
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при проверке категории '{category_name}': {e}")
            return False

    def click_category(self, category_name: str) -> bool:
        """Кликает по категории, чтобы открыть подкатегории."""
        try:
            category = self.page.locator(
                f"li.menu-burger__main-list-item:has-text('{category_name}')"
            )
            if category.count() > 0:
                category.first.click()
                self.page.wait_for_timeout(1000)
                panel = self.page.locator(self.SUBCATEGORY_PANEL)
                if panel.count() > 0:
                    panel.first.wait_for(
                        state="visible",
                        timeout=self.short_timeout
                    )
                    return True
            return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при клике на категорию '{category_name}': {e}")
            return False

    def get_subcategory_texts(self) -> list:
        """Возвращает список текстов подкатегорий."""
        try:
            panel = self.page.locator(self.SUBCATEGORY_PANEL)
            if panel.count() > 0 and panel.first.is_visible():
                texts = []
                for sub in panel.locator("a").all():
                    text = sub.text_content()
                    if text and len(text.strip()) > 0:
                        texts.append(text.strip())
                return texts
            return []
        except PlaywrightTimeoutError:
            return []
        except Exception as e:
            print(f"Ошибка при получении подкатегорий: {e}")
            return []

    def is_subcategory_exists(self, subcategory_name: str) -> bool:
        """Проверяет, существует ли подкатегория."""
        try:
            panel = self.page.locator(self.SUBCATEGORY_PANEL)
            if panel.count() > 0 and panel.first.is_visible():
                sub = panel.locator(f"a:has-text('{subcategory_name}')")
                return sub.count() > 0
            return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Ошибка при проверке подкатегории '{subcategory_name}': {e}")
            return False
