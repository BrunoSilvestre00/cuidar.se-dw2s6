# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from decouple import config as env

LOCAL_DATABASE = env('LOCAL_DATABASE', default=False, cast=bool)

default = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'mydatabase',
} if LOCAL_DATABASE else {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('DB_NAME'),
    'USER': env('DB_USER'),
    'PASSWORD': env('DB_PASSWORD'),
    'HOST': env('DB_HOST'),
    'PORT': env('DB_PORT', cast=int),
}

DATABASES = {
    'default': default
}
