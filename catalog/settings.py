# Global settings for project
import os

# ######### PROJECT PATH CONFIGURATION
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')
PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(PROJECT_DIR)))  # for loggly

# Dotted path to the primary urls file
ROOT_URLCONF = 'catalog.urls'

# Python dotted path to the WSGI application
WSGI_APPLICATION = 'catalog.wsgi.application'
# ######### END PROJECT PATH CONFIGURATION


# ######### DEBUG CONFIGURATION
DEBUG = True
# ######### DEBUG CONFIGURATION


# ######### ADMIN CONTACT CONFIGURATION
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
# ######### END ADMIN CONTACT CONFIGURATION

# ######### AUTH CONFIGURATION
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SHOW_HIJACKUSER_IN_ADMIN = False
# ######### AUTH CONFIGURATION

# ######### GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

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
# ######### END GENERAL CONFIGURATION


# ######### MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION


# ######### STATIC CONFIGURATION
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
# ######### END STATIC CONFIGURATION



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# ######### MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]
# ######### END MIDDLEWARE CONFIGURATION


# ######### TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
            ],
            'debug': False,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]





# ######### FIXTURE CONFIGURATION
FIXTURE_DIRS = [
    os.path.join(PROJECT_DIR, 'fixtures'),
]
# ######### END FIXTURE CONFIGURATION


# ######### APP CONFIGURATION
INSTALLED_APPS = [
    'accounts',
    'authtools',
    'hijack',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'mptt',
    'easy_thumbnails',
    'filer',
    'ckeditor',
    'course',
]

# ######### END APP CONFIGURATION



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}






# ######### CMS CONFIGURATION
LANGUAGES = [
    ('en-us', 'English'),
]

MIGRATION_MODULES = {
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',

    # Added to project for Django 1.7 Support (Remove when app authors support Django 1.7)
    'djangocms_link': 'djangocms_link.migrations_django',
}



########## DJANGO REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 20,                 # Default to 10
    'PAGINATE_BY_PARAM': 'per_page',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100
}
########## END DJANGO REST FRAMEWORK SETTINGS


# ######### COMPRESSOR CONFIG
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]
# ######### END COMPRESSOR CONFIG


# ######### ROBOTS CONFIG
ROBOTS_ENABLED = True
# ######### END ROBOTS CONFIG


# ######### LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': PROJECT_NAME + ' %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        # Send all messages to console, add to loggers for local debugging
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        # Error messages are sent to admin emails
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


# ######### END LOGGING CONFIGURATION


# Need this or you will get warnings with django 1.7
# http://daniel.hepper.net/blog/2014/04/fixing-1_6-w001-when-upgrading-from-django-1-5-to-1-7/
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# # sorl settings
THUMBNAIL_PRESERVE_FORMAT = True

