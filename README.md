# Дипломный проект: Автоматизация тестирования

Автоматизация E2E UI-тестирования Wildberries с использованием Page Object Model (POM).

## Технологический стек
* **Язык программирования:** Python 3.10+
* **Тестовый фреймворк:** Pytest
* **Тестирование UI/API:** Playwright
* **Отчетность:** Allure

## Покрытие (50 сценариев)
* **Поиск (15 тестов):** Поле поиска, Автодополнение, Фильтры, Скролл.
* **Каталог (15 тестов):** Открытие каталога, Категории, Подкатегории, Акции.
* **Карточка товара (20 тестов):** Название, Цена, Корзина, Избранное, Отзывы.

## Инструкция по запуску тестов локально
```bash
git clone https://github.com
cd testd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest
```

## Инструкция по генерации отчётов
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Инструкция по запуску в Docker
```bash
docker build -t diploma-qap .
docker run --rm diploma-qap
```

## Материалы и контакты
* Презентация в папке `docs`.
* Автор: [@lyoshao](https://github.com/lyoshao)
