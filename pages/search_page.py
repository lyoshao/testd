"""Страница результатов поиска."""

from pages.base_page import BasePage


class SearchPage(BasePage):
    """Страница результатов поиска Wildberries."""

    PRODUCT_CARDS = "article.product-card"
    PRODUCT_TITLES = "span.product-card__name"
    FILTER_BUTTON = "button.dropdown-filter__btn--all"
    FILTERS_CONTAINER = "div[class*='filters-desktop']"
    PRODUCT_LIST = "div.product-card-list"

    def __init__(self, page):
        super().__init__(page)

    def get_products_count(self) -> int:
        """Возвращает количество найденных товаров."""
        try:
            container = self.page.locator(self.PRODUCT_LIST)
            if container.count() > 0:
                return container.locator("article.product-card").count()
            return self.page.locator(self.PRODUCT_CARDS).count()
        except Exception:
            return 0

    def get_first_product_title(self) -> str:
        """Возвращает название первого товара."""
        try:
            if self.get_products_count() > 0:
                return self.get_text(self.PRODUCT_TITLES)
        except Exception:
            pass
        return ""

    def get_product_titles_list(self) -> list:
        """Возвращает список названий всех товаров."""
        try:
            titles = self.page.locator(self.PRODUCT_TITLES).all()
            result = []
            for title in titles:
                text = title.text_content()
                if text and len(text.strip()) > 0:
                    result.append(text.strip())
            return result
        except Exception:
            return []

    def click_first_product(self) -> None:
        """Кликает на первый товар в результатах поиска."""
        try:
            if self.get_products_count() > 0:
                self.page.locator(self.PRODUCT_CARDS).first.click()
                self.page.wait_for_load_state("domcontentloaded")
                self.page.wait_for_timeout(5000)
        except Exception:
            pass

    def open_filters(self) -> bool:
        """Открывает панель фильтров."""
        try:
            button = self.page.locator(self.FILTER_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_filters_visible(self) -> bool:
        """Проверяет, видимы ли фильтры."""
        try:
            container = self.page.locator(self.FILTERS_CONTAINER)
            return container.count() > 0 and container.first.is_visible()
        except Exception:
            return False

    def get_filter_count(self) -> int:
        """Возвращает количество доступных фильтров."""
        try:
            container = self.page.locator(self.FILTERS_CONTAINER)
            if container.count() > 0:
                return container.locator("a, button, label").count()
            return 0
        except Exception:
            return 0
