import os

# Путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ для разработки
# Используйте уникальный ключ для разработки
LOCAL_SECRET_KEY = 'your_local_secret_key'

# Режим отладки включен
LOCAL_DEBUG = True  # В продакшн следует установить значение в False

# Допустимые хосты для разработки
LOCAL_ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Настройки базы данных для разработки
LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # Используем SQLite для простоты
    }
}

# Дополнительные настройки для разработки могут быть добавлены здесь
