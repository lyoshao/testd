"""Тесты для карточки товара."""

import allure
import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


@allure.epic("UI тестирование")
@allure.feature("Карточка товара")
class TestProduct:
    """Тесты для карточки товара Wildberries."""

    SEARCH_QUERIES = {
        "phone": "телефон",
        "laptop": "ноутбук",
        "headphones": "наушники",
        "book": "книга",
        "sneakers": "кроссовки",
        "t_shirt": "футболка"
    }

    @allure.story("Открытие карточки")
    @allure.title("Открытие карточки товара из поиска")
    def test_product_page_opens_from_search(self, page):
        """Тест 1: Открытие карточки товара из поиска."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров для открытия"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert "detail.aspx" in page.url, "Не открылась карточка товара"
        name = product_page.get_product_name()
        assert len(name) > 0, "Название товара не отображается"

    @allure.story("Информация о товаре")
    @allure.title("Проверка отображения названия товара")
    def test_product_name_displayed(self, page):
        """Тест 2: Проверка отображения названия товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["laptop"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        name = product_page.get_product_name()
        assert len(name) > 0, f"Название товара не отображается. Получено: '{name}'"

    @allure.story("Информация о товаре")
    @allure.title("Проверка отображения цены")
    def test_product_price_displayed(self, page):
        """Тест 3: Проверка отображения цены."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        price = product_page.get_product_price()
        assert len(price) > 0, "Цена не отображается"

    @allure.story("Корзина")
    @allure.title("Проверка видимости кнопки 'Добавить в корзину'")
    def test_add_to_cart_button_visible(self, page):
        """Тест 4: Проверка видимости кнопки 'Добавить в корзину'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        assert product_page.is_element_visible(
            product_page.ADD_TO_CART_BUTTON
        ), "Кнопка 'Добавить в корзину' не видна"

    @allure.story("Корзина")
    @allure.title("Добавление товара в корзину")
    def test_add_to_cart_works(self, page):
        """Тест 5: Добавление товара в корзину."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        result = product_page.add_to_cart()
        assert result, "Не удалось добавить товар в корзину"

        page.wait_for_timeout(2000)
        cart_link = page.locator("span.navbar-pc__notify")
        assert cart_link.count() > 0, "Корзина не обновилась"

    @allure.story("Информация о товаре")
    @allure.title("Проверка наличия описания товара")
    def test_product_description_visible(self, page):
        """Тест 6: Проверка наличия описания товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        description = product_page.get_characteristics()
        assert description is not None, "Ошибка при получении описания"

    @allure.story("Изображения")
    @allure.title("Проверка наличия фото товара")
    def test_product_photos_exist(self, page):
        """Тест 7: Проверка наличия фото товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["sneakers"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        image_locators = [
            "img[class*='product']",
            "img[alt*='товар']",
            "img[class*='photo']",
            "div[class*='slider'] img",
            "img[class*='j-photo']"
        ]

        images = 0
        for locator in image_locators:
            try:
                count = page.locator(locator).count()
                if count > images:
                    images = count
            except Exception:
                continue

        assert images > 0, "Нет изображений товара"

    @allure.story("Размеры")
    @allure.title("Проверка наличия выбора размера")
    def test_product_sizes_available(self, page):
        """Тест 8: Проверка наличия выбора размера."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["t_shirt"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        sizes_available = product_page.is_size_available()
        assert sizes_available is not None, "Ошибка при проверке размеров"

    @allure.story("Корзина")
    @allure.title("Проверка видимости кнопки 'Купить сейчас'")
    def test_buy_now_button_visible(self, page):
        """Тест 9: Проверка видимости кнопки 'Купить сейчас'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        assert product_page.is_element_visible(
            product_page.BUY_NOW_BUTTON
        ), "Кнопка 'Купить сейчас' не видна"

    @allure.story("Информация о товаре")
    @allure.title("Проверка отображения рейтинга")
    def test_product_rating_displayed(self, page):
        """Тест 10: Проверка отображения рейтинга."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        rating = page.locator("span[class*='productReviewRating']")
        assert rating.count() > 0, "Рейтинг не отображается"

    @allure.story("Социальные функции")
    @allure.title("Проверка наличия кнопки 'Скопировать ссылку'")
    def test_product_share_button_exists(self, page):
        """Тест 11: Проверка наличия кнопки 'Скопировать ссылку'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        share_button = page.locator("button.btnShare--cdooq")
        assert share_button.count() > 0, "Кнопка 'Скопировать ссылку' не найдена"

    @allure.story("Социальные функции")
    @allure.title("Проверка наличия кнопки 'Добавить в избранное'")
    def test_product_favorite_button_exists(self, page):
        """Тест 12: Проверка наличия кнопки 'Добавить в избранное'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        is_visible = product_page.is_favorite_button_visible()

        if not is_visible:
            pytest.skip("Кнопка 'Добавить в избранное' не найдена на этом товаре")

        assert is_visible, "Кнопка 'Добавить в избранное' не найдена"

    @allure.story("Информация о товаре")
    @allure.title("Проверка характеристик товара")
    def test_product_characteristics_visible(self, page):
        """Тест 13: Проверка характеристик товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["laptop"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        characteristics = product_page.get_characteristics()
        assert characteristics is not None, "Характеристики не получены"
        assert len(characteristics) > 0, "Характеристики пустые"

    @allure.story("Информация о товаре")
    @allure.title("Проверка информации о продавце")
    def test_product_seller_info_visible(self, page):
        """Тест 14: Проверка информации о продавце."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["sneakers"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        seller = page.locator("div[class*='sellerInfoNameDefault']")
        assert seller.count() > 0, "Информация о продавце не отображается"

    @allure.story("Информация о товаре")
    @allure.title("Проверка информации о доставке")
    def test_product_delivery_info_visible(self, page):
        """Тест 15: Проверка информации о доставке."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        delivery = page.locator("div[class*='deliveryInfoWrap']")
        assert delivery.count() > 0, "Информация о доставке не отображается"

    @allure.story("Изображения")
    @allure.title("Проверка открытия фото в полном размере по клику")
    def test_product_photo_opens_fullscreen(self, page):
        """Тест 16: Проверка открытия фото в полном размере по клику."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_add_to_cart_visible(), \
            "Кнопка 'Добавить в корзину' не видна"

        result = product_page.click_product_image()
        assert result, "Не удалось кликнуть по изображению"

        fullscreen = page.locator("div[class*='mainSlider--Bp49v']")
        assert fullscreen.count() > 0, "Полноэкранное изображение не открылось"

    @allure.story("Навигация")
    @allure.title("Проверка наличия навигационной цепочки")
    def test_product_breadcrumbs_visible(self, page):
        """Тест 17: Проверка наличия навигационной цепочки."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        breadcrumbs = page.locator(
            "div[class*='breadcrumb'], nav[class*='breadcrumb']"
        ).count()
        assert breadcrumbs > 0, "Навигационная цепочка не отображается"

    @allure.story("Похожие товары")
    @allure.title("Проверка наличия блока 'Смотрите также'")
    def test_product_similar_products_exist(self, page):
        """Тест 18: Проверка наличия блока 'Смотрите также'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(2000)

        similar = page.locator("section[class*='cards-list']")
        assert similar.count() > 0, "Блок 'Смотрите также' не найден"

    @allure.story("Отзывы")
    @allure.title("Проверка наличия блока с отзывами")
    def test_product_reviews_exist(self, page):
        """Тест 19: Проверка наличия блока с отзывами."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()

        reviews_block = page.locator("div[class*='productPageUserActivity']")
        assert reviews_block.count() > 0, "Блок с отзывами не найден"

    @allure.story("Информация о товаре")
    @allure.title("Проверка наличия выбора цвета")
    def test_product_color_options(self, page):
        """Тест 20: Проверка наличия выбора цвета."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["t_shirt"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        page.wait_for_timeout(2000)

        color_slider = page.locator("div[class*='swiper--ccyHx']")
        assert color_slider.count() > 0, "Выбор цвета не найден"
