from .base import *



DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'mathiasdb',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': 'localhost',
         'PORT': '3306'
     }
 }

ENVIRONMENT = 'DEV'
MORE_INFO = 'http://developer.apiluiza.com.br/codigos-de-erro'
