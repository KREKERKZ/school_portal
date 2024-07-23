import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Значения по умолчанию
SECRET_KEY = 'default_secret_key'
DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Подключение приложений
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Приложение школьного портала
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Настройки для использования дефолтного модуля аутентификации
LOGIN_REDIRECT_URL = '/'  # URL для перенаправления после успешного входа
LOGOUT_REDIRECT_URL = '/'  # URL для перенаправления после успешного выхода

# Настройки статических файлов
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# URL-адрес корневого приложения
ROOT_URLCONF = 'config.urls'

# Настройки аутентификации и авторизации
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'app.CustomUser'

# Настройки локализации и времени
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Настройки статических файлов в продакшн
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Пользовательский URL-адрес для входа
LOGIN_URL = '/login/'

# Настройки административной панели
ADMIN_URL = 'admin/'

# Загрузка локальных настроек, если они есть
try:
    from .local_settings import (
        LOCAL_SECRET_KEY,
        LOCAL_DEBUG,
        LOCAL_ALLOWED_HOSTS,
        LOCAL_DATABASES,
    )
    # Обновление значений по умолчанию
    SECRET_KEY = LOCAL_SECRET_KEY
    DEBUG = LOCAL_DEBUG
    ALLOWED_HOSTS = LOCAL_ALLOWED_HOSTS
    DATABASES = LOCAL_DATABASES
except ImportError:
    pass
