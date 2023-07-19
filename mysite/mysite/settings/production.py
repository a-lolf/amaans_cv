from .base import *

DEBUG = False

ALLOWED_HOSTS += ['amaanansari.pythonanywhere.com', 'amaanans.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'amaanansari$portfolio',
        'USER': 'amaanansari',
        'PASSWORD': 'pAri$114',
        'HOST': 'amaanansari.mysql.pythonanywhere-services.com',
    }
}
