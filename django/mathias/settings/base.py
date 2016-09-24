import os

DEBUG = True

VERSION = '1.0.0'

ADMINS = (

)

BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

MANAGERS = ADMINS

SECRET_KEY='j0j33p)77@%y1n5fo1v)%)jg%#!+c($-4m(ai&&ap&n8%81a%_'


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold usuario-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_PATH, '..', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
#STATICFILES_DIRS = (
#    os.path.join(BASE_PATH, 'static'),
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'changeme'

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_PATH, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request',
                'django.core.context_processors.debug',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'EXCEPTION_HANDLER': 'mathias.utils.exceptions.custom_exception_handler',
    'DEFAULT_METADATA_CLASS': 'mathias.utils.metadata.Metadata',
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
       'x-requested-with',
       'content-type',
       'accept',
       'origin',
       'authorization',
       'x-csrftoken',
       'user.password',
   )

SWAGGER_SETTINGS = {
    'api_version': VERSION,
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'token_type': 'Bearer',
    'info': {
        'description': 'mathias platform API.',
        'title': 'mathias',
    },
    'doc_expansion': 'none',
}

ROOT_URLCONF = 'mathias.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mathias.wsgi.application'


#APPS

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework.authtoken',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
]

PROJECT_APPS = [
    'mathias.valeu',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'logstash': {
          'class': 'logstash.TCPLogstashHandler',
          'host': 'log.burzum.appsluiza.com.br',
          'port': 5030,
          'version': 1,
          'message_type': 'logstash',
          'fqdn': False
      }
    },
    'loggers': {
        '': {
            'handlers': ['logstash'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

BZTOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJ0cmFuc2Zvcm1lcnMtd2l0d2lja3kiLCJ0ZWFtIjoiZnVsZmlsbG1lbnQifQ.So7woHWjxoGUAXSzlleajjmLTpUZnMOaVRTIfrbaoRQ'
