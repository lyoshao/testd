"""Страница карточки товара."""

from pages.base_page import BasePage


class ProductPage(BasePage):
    """Карточка товара Wildberries."""

    # Локаторы
    PRODUCT_NAME = "h2[class*='mo-typography_variant_title3']"
    PRODUCT_PRICE = "span[class*='priceBlockPrice'] ins"
    ADD_TO_CART_BUTTON = "button[aria-label='Добавить в корзину']"
    BUY_NOW_BUTTON = "button[aria-label='Купить сейчас']"
    FAVORITE_BUTTON = "button[class*='toFavourite'][class*='favouriteButton']"
    SHOW_DETAILS_BUTTON = "button[class*='btnDetail']"
    PRODUCT_CHARACTERISTICS = "div.content--zb_r9"
    SIZE_LIST = "ul.sizesList--EwFfe"
    PRODUCT_IMAGE = "div[class*='imageContainer'] img"

    def __init__(self, page):
        super().__init__(page)

    def get_product_name(self) -> str:
        """Получает название товара."""
        try:
            element = self.page.locator(self.PRODUCT_NAME)
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def get_product_price(self) -> str:
        """Получает цену товара."""
        try:
            element = self.page.locator(self.PRODUCT_PRICE)
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def add_to_cart(self) -> bool:
        """Добавляет товар в корзину."""
        try:
            button = self.page.locator(self.ADD_TO_CART_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1500)
                return True
            return False
        except Exception:
            return False

    def buy_now(self) -> bool:
        """Нажимает на кнопку 'Купить сейчас'."""
        try:
            button = self.page.locator(self.BUY_NOW_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def show_details(self) -> bool:
        """Нажимает на кнопку, чтобы показать характеристики."""
        try:
            button = self.page.locator(self.SHOW_DETAILS_BUTTON)
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def get_characteristics(self) -> str:
        """Получает характеристики товара."""
        try:
            self.show_details()
            element = self.page.locator(self.PRODUCT_CHARACTERISTICS)
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def is_size_available(self) -> bool:
        """Проверяет, есть ли выбор размера."""
        try:
            size_list = self.page.locator(self.SIZE_LIST)
            return size_list.count() > 0 and size_list.first.is_visible()
        except Exception:
            return False

    def select_size(self, size: str) -> bool:
        """Выбирает размер товара."""
        try:
            sizes = self.page.locator(f"{self.SIZE_LIST} button").all()
            for size_btn in sizes:
                btn_text = size_btn.text_content()
                if btn_text is not None and size in btn_text:
                    size_btn.click()
                    self.page.wait_for_timeout(500)
                    return True
        except Exception:
            pass
        return False

    def add_to_favorites(self) -> bool:
        """Добавляет товар в избранное."""
        try:
            button = self.page.locator(self.FAVORITE_BUTTON)
            if button.count() > 0 and button.first.is_visible():
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_favorite_button_visible(self) -> bool:
        """Проверяет, видима ли кнопка 'Добавить в избранное'."""
        try:
            return self.is_element_visible(self.FAVORITE_BUTTON)
        except Exception:
            return False

    def is_add_to_cart_visible(self) -> bool:
        """Проверяет, видима ли кнопка 'Добавить в корзину'."""
        try:
            return self.is_element_visible(self.ADD_TO_CART_BUTTON)
        except Exception:
            return False

    def click_product_image(self) -> bool:
        """Кликает по изображению товара."""
        try:
            image = self.page.locator(self.PRODUCT_IMAGE)
            if image.count() > 0:
                image.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_size_popup_visible(self) -> bool:
        """Проверяет, видима ли плашка с выбором размера."""
        try:
            popup = self.page.locator("div[class*='popupNarrow']")
            return popup.count() > 0 and popup.first.is_visible()
        except Exception:
            return False

    def is_cart_opened(self) -> bool:
        """Проверяет, открылась ли корзина."""
        try:
            return "cart" in self.page.url.lower()
        except Exception:
            return False

    def close_size_popup(self) -> bool:
        """Закрывает плашку с выбором размера."""
        try:
            close_button = self.page.locator("button[class*='popup__close']")
            if close_button.count() > 0:
                close_button.first.click()
                self.page.wait_for_timeout(500)
                return True
            return False
        except Exception:
            return False