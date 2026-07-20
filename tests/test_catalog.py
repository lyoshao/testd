"""Тесты для каталога."""

import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI тестирование")
@allure.feature("Каталог")
class TestCatalog:
    """Тесты для каталога Wildberries."""

    # Категории, у которых точно есть подкатегории
    CATEGORIES_WITH_SUB = [
        "Женщинам",
        "Мужчинам",
        "Электроника",
        "Дом",
        "Спорт",
        "Акции"
    ]

    @allure.story("Кнопка каталога")
    @allure.title("Проверка наличия кнопки каталога")
    def test_catalog_button_exists(self, page):
        """Тест 1: Проверка наличия кнопки каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        button = page.locator("button[data-wba-header-name='Catalog']")
        assert button.count() > 0, "Кнопка каталога не найдена"

    @allure.story("Кнопка каталога")
    @allure.title("Проверка видимости кнопки каталога")
    def test_catalog_button_visible(self, page):
        """Тест 2: Проверка видимости кнопки каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        button = page.locator("button[data-wba-header-name='Catalog']")
        assert button.is_visible(), "Кнопка каталога не видна"

    @allure.story("Панель каталога")
    @allure.title("Проверка открытия панели каталога")
    def test_catalog_panel_opens(self, page):
        """Тест 3: Проверка открытия панели каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        result = main_page.open_catalog()
        assert result, "Не удалось открыть панель каталога"
        assert main_page.is_catalog_panel_open(), "Панель каталога не открылась"

    @allure.story("Панель каталога")
    @allure.title("Проверка наличия категорий в панели")
    def test_catalog_panel_has_categories(self, page):
        """Тест 4: Проверка наличия категорий в панели."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()
        categories = main_page.get_catalog_categories()
        assert len(categories) > 0, "В панели каталога нет категорий"

    @allure.story("Панель каталога")
    @allure.title("Проверка появления подкатегорий при клике на категорию")
    def test_catalog_panel_has_subcategories(self, page):
        """Тест 5: Проверка появления подкатегорий при клике на категорию."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        found_subcategories = False
        for category in self.CATEGORIES_WITH_SUB:
            if main_page.is_category_exists(category):
                if main_page.click_category(category):
                    subcategories = main_page.get_subcategory_texts()
                    if len(subcategories) > 0:
                        found_subcategories = True
                        break

        assert found_subcategories, "Не удалось найти подкатегории ни для одной категории"

    @allure.story("Панель каталога")
    @allure.title("Проверка закрытия панели каталога")
    def test_catalog_panel_close(self, page):
        """Тест 6: Проверка закрытия панели каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        assert main_page.is_catalog_panel_open(), "Панель не открылась"
        main_page.close_catalog()
        page.wait_for_timeout(1000)
        assert not main_page.is_catalog_panel_open(), "Панель не закрылась"

    @allure.story("Категории")
    @allure.title("Проверка наличия категории {category}")
    @pytest.mark.parametrize("category", [
        "Электроника",
        "Дом",
        "Красота",
        "Спорт",
        "Бренды"
    ])
    def test_catalog_panel_has_category(self, page, category):
        """Тесты 7-11: Проверка наличия конкретных категорий."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()
        assert main_page.is_category_exists(category), f"Категория '{category}' не найдена"

    @allure.story("Категории")
    @allure.title("Проверка наличия категорий одежды")
    def test_catalog_panel_has_clothing(self, page):
        """Тест 12: Проверка наличия категорий одежды."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        has_clothing = (
            main_page.is_category_exists("Одежда") or
            main_page.is_category_exists("Женщинам") or
            main_page.is_category_exists("Мужчинам")
        )
        assert has_clothing, "Категория одежды не найдена"

    @allure.story("Категории")
    @allure.title("Проверка наличия категорий для детей")
    def test_catalog_panel_has_children(self, page):
        """Тест 13: Проверка наличия категорий для детей."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        has_children = (
            main_page.is_category_exists("Детям") or
            main_page.is_category_exists("Игрушки")
        )
        assert has_children, "Категория 'Детям' не найдена"

    @allure.story("Категории")
    @allure.title("Проверка наличия раздела со скидками")
    def test_catalog_panel_has_sale(self, page):
        """Тест 14: Проверка наличия раздела со скидками."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        has_sale = (
            main_page.is_category_exists("Распродажа") or
            main_page.is_category_exists("Акции") or
            main_page.is_category_exists("Скидки WB Клуба")
        )
        assert has_sale, "Раздел со скидками не найден"

    @allure.story("Категории")
    @allure.title("Клик по категории 'Акции' и проверка страницы акций")
    def test_catalog_panel_click_promotions(self, page):
        """Тест 15: Клик по категории 'Акции' и проверка страницы акций."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        if not main_page.is_category_exists("Акции"):
            pytest.skip("Категория 'Акции' не найдена")

        promotions_link = page.locator(
            "li.menu-burger__main-list-item a:has-text('Акции')"
        )
        assert promotions_link.count() > 0, "Ссылка на 'Акции' не найдена"

        expected_url = "https://www.wildberries.by/promotions"
        promotions_link.first.click()
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(2000)

        assert page.url == expected_url or page.url.startswith(expected_url), \
            f"Ожидалось: {expected_url}, Получено: {page.url}"

        banner = page.locator("img[alt='Сделано в Беларуси']")
        assert banner.count() > 0, "Баннер 'Сделано в Беларуси' не найден"
        assert banner.first.is_visible(), "Баннер 'Сделано в Беларуси' не видим"

        width = banner.first.get_attribute("width")
        height = banner.first.get_attribute("height")
        assert width == "660", f"Неверная ширина баннера: {width}"
        assert height == "210", f"Неверная высота баннера: {height}"
