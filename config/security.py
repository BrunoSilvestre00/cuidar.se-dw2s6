from decouple import config as env

SECRET_KEY = env('SECRET_KEY')

HOSTS = ['*']

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
