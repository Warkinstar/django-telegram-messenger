# django-telegram-messenger

### Адрес сайта: https://message-duplicator.fly.dev/
### Бот: https://t.me/MessageDuplicationBot
### Узнать свой telegram id: https://t.me/getmyid_bot

Принимает сообщение пользователя по API и дублирует его в телеграм бот сайта на который подписан пользователь.
Имеется документация Swagger UI и Redoc. Предоставляет API точки для регистрации, входа-выхода, создания и отправки 
сообщения в telegram-bot и др. При регистрация пользователь должен обязательно указать свой настойящий пользовательский ID телеграмма и активировать бота сайта(ссылка выше) иначе дублирование сообщений не будет выполняться.

Project


# Установка

* Создаем виртуальное окружение
```
python -m venv .venv
.venv/scripts/activate
```

* Устанавливаем зависимости проекта
pip install -r requirements.txt

* Создайте файл .env для установки переменных сред:
```env
# .env
DEBUG = True
SECRET_KEY = "YOUR-SECRET-KEY"

DJANGO_SECURE_SSL_REDIRECT = False


DJANGO_SECURE_HSTS_SECONDS = 0
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS = False
DJANGO_SECURE_HSTS_PRELOAD = False


DJANGO_SESSION_COOKIE_SECURE = False
DJANGO_CSRF_COOKIE_SECURE = False

TELEGRAM_BOT_TOKEN = "YOUR-TELEGRAM-BOT-TOKEN"
```

* В .env укажите токен вашего телеграм бота, создать бота можно тут https://t.me/BotFather


* Проведите миграцию базы данных:
```
python manage.py migrate
```

* Создайте superuser:
```
python manage.py creatsuperuser
```

* Запуск проекта:
```
python manage.py runserver
```

### Использование

Регистрация:
![Регистрация](https://raw.githubusercontent.com/Warkinstar/screenshots/main/django-telegram-messenger/Login.png)

Вход:
![Вход](https://storage.cloud.google.com/bucket-django-educa/django-telegram-messanger/Login.png)

Телеграм Бот и отправка сообщений
![Телеграм Бот](https://storage.cloud.google.com/bucket-django-educa/django-telegram-messanger/send_messages.png)


## Лицензия
Этот проект лицензирован в соответствии с лицензией MIT. Подробности можно найти в файле [LICENSE](LICENSE).
