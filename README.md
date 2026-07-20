# Дипломный проект: Автоматизация тестирования

Автоматизация E2E UI-тестирования (Wildberries) и API (Fake Store API) с использованием Page Object Model (POM).

## Технологический стек
* **Язык программирования:** Python 3.10+
* **Тестовый фреймворк:** Pytest
* **Тестирование UI/API:** Playwright, Requests
* **Отчетность:** Allure

## Покрытие (55 сценариев)
* **UI (50 тестов):** Поиск (15), Каталог (15), Карточка товара (20).
* **API (5 тестов):** CRUD операции (GET/POST), авторизация, SQLite.

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
docker build -t Diploma-QAP
docker run --rm Diploma-QAP
```

## Материалы и контакты
* Презентация в папке `docs`.
* Автор: [@lyoshao](https://github.com)