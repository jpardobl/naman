# Django settings for naman project.
import django.conf.global_settings as DEFAULT_SETTINGS
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#constantes maestras
ROLE_BD = 'BD'
ROLE_SW = 'SW'
ROLE_SA = 'SA'

ENV_PROD = "PRO"
# end constantes maestras

from django.contrib import messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
    }



ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev2.sqlite',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },
#    'redip': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'redip',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
#        'USER': 'root',
#        'PASSWORD': 'wredp',
#        'HOST': '172.22.2.69',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#        'PORT': '',                      # Set to empty string for default.
#     },
#    'bahamas': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'bahamas',                      # Or path to database file if using sqlite3.
#        # The following settings are not used with sqlite3:
#        'USER': 'inma',
#        'PASSWORD': 'serafin2011',
#        'HOST': '172.22.2.150',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#        'PORT': '',                      # Set to empty string for default.
#    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

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

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b!7exo7!kwtfi1_19zhl)i6rp54jopod)oc$ig0ygxj5c+cemb'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'naman.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'naman.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "tools.views.content_procesor_referer",
)

RESULTS_PER_PAGE = 12
LOGIN_URL = '/login'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
    'web',
    "south",
    "django_extensions",
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

from logging.handlers import SysLogHandler
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'verbose': {
            'format': 'IPAM: %(message)s'
        },
        'request': {
		'format': 'IPAM: %(status_code)d %(request)s %(message)s'
	},
	'db': {
		'format': 'IPAM: %(duration)d %(sql)s'
	}
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        },
	'syslog':{
      	  	'level':'WARN',
        	'class': 'logging.handlers.SysLogHandler',
        	'formatter': 'verbose',
        	'facility': SysLogHandler.LOG_LOCAL7,
        	'address': '/dev/log',
    	},
	'syslog_request':{
                'level':'WARN',
                'class': 'logging.handlers.SysLogHandler',
                'formatter': 'request',
                'facility': SysLogHandler.LOG_LOCAL7,
                'address': '/dev/log',
        },
	'syslog_db':{
                'level':'WARN',
                'class': 'logging.handlers.SysLogHandler',
                'formatter': 'db',
                'facility': SysLogHandler.LOG_LOCAL7,
                'address': '/dev/log',
        },
    },
    'loggers': {
	'': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['syslog_request'],
            'level': 'DEBUG',
            'propagate': False,
        },
	'django.db.backends': {
            'handlers': ['syslog_db'],
            'level': 'DEBUG',
            'propagate': False,
        },

    }
}



REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'PAGINATE_BY': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "django.contrib.auth.models.AnonymousUser",
     #  'rest_framework.authentication.BasicAuthentication',
  #      'rest_framework.authentication.SessionAuthentication',
    ),
}


# Active directory auth ******************
# settings.py
# active directory authentication module
AD_DNS_NAME = 'iberia.ib'	 # FQDN of your DC (using just the Domain Name to utilize all DC's)
# If using non-SSL use these
AD_LDAP_PORT=389
AD_LDAP_URL='ldap://%s:%s' % (AD_DNS_NAME,AD_LDAP_PORT)
# If using SSL use these:
#AD_LDAP_PORT=636
#AD_LDAP_URL='ldaps://%s:%s' % (AD_DNS_NAME,AD_LDAP_PORT)
AD_SEARCH_DN = 'OU=People,dc=iberia,dc=ib'
AD_NT4_DOMAIN = 'iberia.ib'
AD_SEARCH_FIELDS = ['mail','givenName','sn','sAMAccountName','memberOf']
AD_MEMBERSHIP_ADMIN = ['ArqServidor (Cambio)']	# this ad group gets superuser status in django
# only members of this group can access
AD_MEMBERSHIP_REQ = AD_MEMBERSHIP_ADMIN + ['DesRed (Lectura)', 'sistemas', ]
AD_CERT_FILE = '/tmp/cert'	# this is the certificate of the Certificate Authority issuing your DCs certificate
AD_DEBUG=True #Set to false for prod, Slows things down ALOT
AD_DEBUG_FILE='/tmp/ldap.debug'


AUTHENTICATION_BACKENDS = (
     #'core.backend.ActiveDirectoryAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend', #Comment out to prevent authentication from DB
)
