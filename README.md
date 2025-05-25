# KURS Service — Автосервис на Django

## О проекте

KURS Service — это комплексный веб-сервис для автосервиса, реализованный на Django. Проект включает:

- Онлайн-запись на обслуживание
- Каталог услуг и прайс-листы
- Система отзывов
- Галерея работ
- Новости и акции
- Личный кабинет пользователя
- Интеграция с корзиной и чек-листом
- Админ-панель для управления контентом

## Основные возможности

- Многоуровневое меню услуг
- Динамическая фильтрация и пагинация прайса
- AJAX-запросы для подгрузки моделей/модификаций авто
- Система скидок и акций
- Отзывы клиентов
- Интерактивная галерея
- Адаптивный дизайн (Bootstrap)
- Интеграция с Яндекс.Картами

## Структура проекта

- `kurs_service/` — основной Django-проект
- Приложения: `base_page`, `main_page`, `photo_gallery`, `discounts`, `evacuation`, `insurance`, `online_appointment`, `price_maintenance`, `check_list` и др.
- `static/` — статика (CSS, JS, изображения)
- `media/` — пользовательские файлы и изображения

## Установка и запуск

1. **Клонирование репозитория**

   ```bash
   git clone <repo-url>
   cd kurs-service
   ```

2. **Создание и активация виртуального окружения**

   - **Windows:**

     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1

     ```

   - **Linux/macOS:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка переменных окружения**

   Создайте файл `.env` в корне проекта и укажите параметры подключения к MySQL:

   ```plaintext
   DB_NAME=kurs_service
   DB_USER=your_user
   DB_PASS=your_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

5. **Миграции и создание суперпользователя**

   ```bash
   python kurs_service/manage.py migrate
   python kurs_service/manage.py createsuperuser
   ```

6. **Запуск сервера**

   ```bash
   python kurs_service/manage.py runserver
   ```

7. **Доступ к сайту**

   - Сайт: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Админка: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Зависимости

- Django 5.1.7
- PyMySQL
- Pillow
- django-debug-toolbar
- Bootstrap, jQuery, FontAwesome (в static)
- Подробный список — [requirements.txt](requirements.txt)

## Документация

- [Структура БД](docs/database.md)
- [Описание приложений](docs/apps.md)
- [Работа с медиа и статикой](docs/static_media.md)
- [Инструкция для администратора](docs/admin_guide.md)

## Лицензия

См. файл [LICENCE](LICENCE)

---

> Для подробной информации по каждому модулю и настройке см. документацию в папке [docs/](docs/).
