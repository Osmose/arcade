# Django settings for captain project common to all environments.
import os
from os.path import dirname

from django.utils.functional import lazy


# Utilities
##############################################################################
ROOT = dirname(dirname(dirname(os.path.abspath(__file__))))
def path(*a):
    return os.path.join(ROOT, *a)


# Django Settings
##############################################################################

# The following settings are overridden and documented in local.py.
ADMINS = ()
DATABASES = {}
DEBUG = True
MANAGERS = ADMINS
SECRET_KEY = ''
TEMPLATE_DEBUG = DEBUG

# List of hostnames that users are allowed to access your site through.
def _allowed_hosts():
    """Determine ALLOWED_HOSTS based on SITE_URL."""
    from django.conf import settings
    from urlparse import urlparse

    host = urlparse(settings.SITE_URL).netloc  # Remove protocol and path
    host = host.rsplit(':', 1)[0]  # Remove port
    return [host]
ALLOWED_HOSTS = lazy(_allowed_hosts, list)()

# L10n
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False

# Timezones
USE_TZ = True

# Static and uploaded media.
MEDIA_ROOT = path('media')
MEDIA_URL = '/media/'
STATIC_ROOT = path('static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.request',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'django_browserid.context_processors.browserid',
)

ROOT_URLCONF = 'arcade.urls'

WSGI_APPLICATION = 'arcade.wsgi.application'

INSTALLED_APPS = (
    'arcade.base',
    'arcade.users',
    'arcade.games',

    'django_browserid',
    'south',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Third-party Libary Settings
##############################################################################

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'browserid',
]
