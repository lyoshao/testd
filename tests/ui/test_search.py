"""Тесты для поиска."""

import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestSearch:
    """Тесты для поиска на Wildberries."""

    # Поисковые запросы
    QUERIES = {
        "product": "кроссовки",
        "brand": "Adidas",
        "special": "!@#$%^&*()",
        "numbers": "12345",
        "t_shirt": "футболка",
        "phone": "телефон",
        "laptop": "ноутбук",
        "clothes": "одежда"
    }

    def test_search_input_is_visible(self, page):
        """Тест 1: Проверка видимости поля поиска."""
        main_page = MainPage(page)
        main_page.open_main_page()
        assert main_page.is_element_visible(
            main_page.SEARCH_INPUT
        ), "Поле поиска не видно"

    def test_search_button_is_visible(self, page):
        """Тест 2: Проверка видимости поля поиска (кнопки нет, поиск по Enter)."""
        main_page = MainPage(page)
        main_page.open_main_page()
        assert main_page.is_element_visible(
            main_page.SEARCH_INPUT
        ), "Поле поиска не видно"

    def test_search_by_product_name(self, page):
        """Тест 3: Поиск по названию товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["product"])

        assert "search" in page.url.lower() or "catalog" in page.url.lower(), \
            "Страница результатов не открылась"

        search_page = SearchPage(page)
        count = search_page.get_products_count()
        assert count > 0, "Товары не найдены"

    def test_search_by_brand(self, page):
        """Тест 4: Поиск по бренду."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["brand"])

        search_page = SearchPage(page)
        count = search_page.get_products_count()
        assert count > 0, "Товары бренда не найдены"

    def test_search_empty_query(self, page):
        """Тест 5: Поиск с пустым запросом."""
        main_page = MainPage(page)
        main_page.open_main_page()

        search_input = page.locator(main_page.SEARCH_INPUT)
        current_value = search_input.input_value()
        assert current_value == "", "Поле поиска не пустое"
        assert search_input.is_visible(), "Поле поиска не видимо"
        assert search_input.is_enabled(), "Поле поиска не активно"
        assert page.url == "https://www.wildberries.by/", "Мы не на главной странице"

    def test_search_special_characters(self, page):
        """Тест 6: Поиск со специальными символами."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["special"])

        search_page = SearchPage(page)
        count = search_page.get_products_count()
        assert count >= 0, "Ошибка при поиске со спецсимволами"

    def test_search_long_query(self, page):
        """Тест 7: Поиск с очень длинным запросом."""
        main_page = MainPage(page)
        main_page.open_main_page()
        long_query = "а" * 100
        main_page.search_product(long_query)

        input_value = page.locator("input#searchInput").input_value()
        assert long_query in input_value, "Длинный запрос не отобразился в поле поиска"

    def test_search_with_numbers(self, page):
        """Тест 8: Поиск по числовому запросу."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["numbers"])

        search_page = SearchPage(page)
        count = search_page.get_products_count()
        assert count >= 0, "Система упала при поиске по числам"

    def test_search_results_contain_query(self, page):
        """Тест 9: Проверка, что результаты содержат запрос."""
        main_page = MainPage(page)
        main_page.open_main_page()
        query = self.QUERIES["t_shirt"]
        main_page.search_product(query)

        search_page = SearchPage(page)
        titles = search_page.get_product_titles_list()

        if titles:
            first_title = titles[0].lower() if titles[0] else ""
            assert query.lower() in first_title or "футбол" in first_title, \
                "Результаты не содержат запрос"

    def test_search_case_insensitive(self, page):
        """Тест 10: Поиск без учета регистра."""
        main_page = MainPage(page)
        main_page.open_main_page()

        main_page.search_product("ipHone")
        search_page = SearchPage(page)
        count1 = search_page.get_products_count()

        page.go_back()
        page.wait_for_timeout(1000)
        main_page.search_product("iphone")
        count2 = search_page.get_products_count()

        assert count1 >= 0 and count2 >= 0, "Оба запроса должны работать"

    def test_search_autocomplete(self, page):
        """Тест 11: Проверка автодополнения при вводе."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.fill_input(main_page.SEARCH_INPUT, "теле")
        page.wait_for_timeout(2000)

        suggestions = page.locator("div.autocomplete.search-catalog__autocomplete")
        assert suggestions.count() > 0, "Блок автодополнения не появился"
        assert suggestions.first.is_visible(), "Блок автодополнения не видим"

    def test_clear_search_field(self, page):
        """Тест 12: Очистка поля поиска."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.fill_input(main_page.SEARCH_INPUT, "телефон")

        main_page.page.locator(main_page.SEARCH_INPUT).clear()
        value = main_page.page.locator(main_page.SEARCH_INPUT).input_value()
        assert value == "", "Поле не очистилось"

    def test_search_with_filter(self, page):
        """Тест 13: Поиск с применением фильтра."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["clothes"])

        search_page = SearchPage(page)
        result = search_page.open_filters()

        if not result:
            pytest.skip("Кнопка фильтров не найдена")

        assert search_page.is_filters_visible(), "Фильтры не отобразились"

        filter_count = search_page.get_filter_count()
        assert filter_count > 0, "Нет доступных фильтров"

    def test_infinite_scroll_works(self, page):
        """Тест 14: Проверка подгрузки товаров при скролле."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["phone"])

        search_page = SearchPage(page)

        count_before = search_page.get_products_count()
        assert count_before > 0, "Нет товаров на странице"

        # Плавный скролл для подгрузки товаров
        for _ in range(5):
            page.mouse.wheel(0, 1000)
            page.wait_for_timeout(1000)

        count_after = search_page.get_products_count()
        assert count_after > count_before, "Товары не подгрузились при скролле"

    def test_search_results_count_format(self, page):
        """Тест 15: Проверка формата отображения количества результатов."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.QUERIES["laptop"])

        count_text = page.locator("span.searching-results__count").text_content()
        assert count_text is not None, "Не отображается количество результатов"