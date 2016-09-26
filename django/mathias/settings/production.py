from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE_NAME', 'witwicky'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', ''),
        'HOST': os.environ.get('MYSQL_HOST', ''),
        'PORT': os.environ.get('MYSQL_PORT', '')
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'p6pqtha3ukrdv7zn',
#         'USER': 'jgr5fnsjooyqgr3f',
#         'PASSWORD': 'uccthavhuugg2tgp',
#         'HOST': 'sp6xl8zoyvbumaa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
#         'PORT': 3306
#     }
# }

ENVIRONMENT = 'PROD'


MORE_INFO = 'http://developer.apiluiza.com.br/codigos-de-erro'
