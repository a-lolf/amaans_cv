from .base import *

DEBUG = False

ALLOWED_HOSTS += ['amaanansari.pythonanywhere.com', 'amaanans.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_portfolio',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
    }
}
