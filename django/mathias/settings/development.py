from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'dev.db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

ENVIRONMENT = 'DEV'


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'mathiasdb',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': 'localhost',
         'PORT': '3306',
         'CONN_MAX_AGE': None
     }
 }

MORE_INFO = 'http://developer.apiluiza.com.br/codigos-de-erro'
