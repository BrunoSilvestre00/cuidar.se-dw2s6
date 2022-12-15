from decouple import config as env
from corsheaders.defaults import default_headers

SECRET_KEY = env('SECRET_KEY')

HOSTS = ['*']

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = default_headers + ('Token', 'Language')

CSRF_COOKIE_NAME = "csrftoken"

DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_THROTTLE_RATES': {
        'low-minute-user': '6/minute',
        'low-second-user': '3/second',
    }
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
