FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]