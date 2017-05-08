
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '04gsy@^%nl65zhru42)n&9b20z#ep_rvfr@rj@8+wf+c423!p='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# This has been used in development to allow the unrecognized Domain.

ALLOWED_HOSTS = []


# All the Modules which have been installed on the website must be listed .

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HotelApp',
    'ManageHotels',
    'wkhtmltopdf',
    'Authorize',
    'rest_framework',
    'Reservations',
    'registration',
    'django.contrib.sites',
    #All auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #Auth providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
]

#A Url has been designated to the development site "checkin.com" , this id tells django regarding the domain.
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HotelProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Installed to handle media files.
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'HotelProject.wsgi.application'


# Database
# Modify accoding to database preference.

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'husainfour',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

## Django and All Auth backends which handle Registration / Social registration and Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Internationalization


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


# Inform Django of the Static and Root paths for serving static files
STATICFILES_DIRS = [STATIC_DIR,]
STATIC_URL = '/static/'
STATIC_ROOT = 'static_cdn'

#Django Registration redux settings.
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL = '/accounts/login/'
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/Authorize/'
REGISTRATION_EMAIL_HTML = False

# Media URL and Root settings to allow uploading images.
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
