from ctypes import cast
from os import path
from decouple import config as env

BASE_DIR = path.dirname(path.dirname(__file__))
# BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
if env('DEBUG', default=False, cast=bool): 
    STATIC_ROOT = path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = (
        path.join(BASE_DIR,  'core', 'assets'),
    )
else:
    STATIC_ROOT = path.join(BASE_DIR,  'core', 'assets')