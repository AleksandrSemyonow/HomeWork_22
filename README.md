### 📌 Основной функционал

1. - Инициализирован Django-проект **`config`**.
2. - Настроено виртуальное окружение с помощью **Poetry**.
3. - Создано приложение **`catalog`** и зарегистрировано в `INSTALLED_APPS` конфигурации.
4. - Настроена маршрутизация в файле `config/urls.py`.
5. - Созданы два HTML-шаблона:  
   -  `home` — домашняя страница  
   -  `contacts` — страница с контактной информацией
6. - Для указанных шаблонов созданы контроллеры (views) и настроены маршруты.


## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:AleksandrSemyonow/HomeWork_22.git
   ```

2. Установите Poetry (если ещё не установлен):  
   [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

3. Установите зависимости:
   ```bash
   poetry install
   ```

4. Активируйте виртуальное окружение:
   ```bash
   poetry shell
   ```

5. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
   