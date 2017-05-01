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

SLACK = {
    'token': os.environ.get('SLACK_TOKEN', ''),
    'host': os.environ.get('SLACK_HOST', ''),
    'channel_id': os.environ.get('SLACK_CHANNEL_ID'),
    'leaderboard_url': os.environ.get('SLACK_LEADERBOARD_URL'),
    'icon_url': os.environ.get('SLACK_ICON_URL'),
    'app_name': os.environ.get('SLACK_APP_NAME'),
}

ENVIRONMENT = 'STAGE'

MORE_INFO = 'http://developer.apiluiza.com.br/codigos-de-erro'
