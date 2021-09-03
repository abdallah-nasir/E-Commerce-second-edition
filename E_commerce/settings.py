"""
Django settings for E_commerce project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import django_heroku
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^yvdhx^w5$jah)-p!vbbqy5vf9qco&ge)p0m^nr_p%$=4&6i56'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#TEMPLATE_DEBUG = DEBUG
if DEBUG == False:
    TEMPLATE_DEBUG = DEBUG
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT=True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD =True
    SESSION_COOKIE_PATH = '/;HttpOnly'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True 
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_HSTS_INCLUDE_SUBDOMAINS =True
    
    
ALLOWED_HOSTS =["127.0.0.1","localhost","ludus-ecommerce.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # myapps
    "STORE",
    # packages
    'crispy_forms',
    'bootstrap_datepicker_plus',   
    'django_filters',
    "cities_light",
    "ajax_select",
    'ckeditor',
    'ckeditor_uploader',
   
    # "Pay_Mob",
    # "django_countries",
    'allauth',         
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]       

     
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware"

]

ROOT_URLCONF = 'E_commerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',   
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "STORE.processors.global_context",
                "STORE.processors.global_profile",
                "STORE.processors.global_PayMob",
                "STORE.processors.global_wishlist",
    
            ],
        }, 
    },     
]

WSGI_APPLICATION = 'E_commerce.wsgi.application'




#COUNTRIES
# COUNTRIES_ONLY = ["SA","EG","AE"]
      
#cities
# CITIES_LIGHT_APP_NAME = 'STORE'

CITIES_LIGHT_TRANSLATION_LANGUAGES = ["ara","en"]
CITIES_LIGHT_INCLUDE_COUNTRIES = ["EG","AE","SA"]
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT',]
# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
# "Email Backend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'abdullahnasser6@gmail.com'
EMAIL_HOST_PASSWORD ="bbvpxmxneyglgqzt"
EMAIL_USE_TLS = True
EMAIL_USE_SSL= False
EMAIL_PORT = '587'
#allauth  
SITE_ID=1
LOGIN_REDIRECT_URL ="home:home"
ACCOUNT_ADAPTER="allauth.account.adapter.DefaultAccountAdapter"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL=LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL =None
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_CONFIRMATION_HMAC =True
ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_EMAIL_VERIFICATION ="mandatory"   
ACCOUNT_EMAIL_SUBJECT_PREFIX ="Site"
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN =120
ACCOUNT_EMAIL_MAX_LENGTH=245
ACCOUNT_MAX_EMAIL_ADDRESSES=1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT =3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =120
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True
ACCOUNT_LOGOUT_ON_GET =False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =True
ACCOUNT_LOGIN_ON_PASSWORD_RESET =True
ACCOUNT_LOGOUT_REDIRECT_URL ="home:home"
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =True
ACCOUNT_PRESERVE_USERNAME_CASING =False
ACCOUNT_SESSION_REMEMBER =None
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =True
ACCOUNT_SIGNUP_REDIRECT_URL =LOGIN_REDIRECT_URL
# ACCOUNT_USERNAME_BLACKLIST (=[])
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_USERNAME_MIN_LENGTH =5
ACCOUNT_USERNAME_REQUIRED =True
SOCIALACCOUNT_AUTO_SIGNUP =True
SOCIALACCOUNT_EMAIL_VERIFICATION =ACCOUNT_EMAIL_VERIFICATION
SOCIALACCOUNT_EMAIL_REQUIRED =ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_QUERY_EMAIL =ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_STORE_TOKENS =False
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id':"1026393978710-192vg587ftturb4mr1polgvm3s4ubvfa.apps.googleusercontent.com",
            'secret':"Qsfxt18kpU_BfrAipW6TN0dK",
            'key': ''
        }
    },

    'facebook': {
    # For each OAuth based provider, either add a ``SocialApp``
    # (``socialaccount`` app) containing the required client
    # credentials, or list them here:
    'APP': {
        'client_id':"2913945832252864",
        'secret':"6b6c9520c639e0f62e1b4c68c0a5f81f",
        'key': '',
       
    }
}
}
ACCOUNT_FORMS = {
    'signup': 'STORE.forms.MyCustomSignupForm',

}
AUTHENTICATION_BACKENDS = [
    # ............
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    #      ...
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES={
    "default":{
        "ENGINE":"django.db.backends.postgresql_psycopg2",
        "NAME":"deqdvj9oqtl78t",
        "USER":"yiqxgupmlcyarh",
        "PASSWORD":"27c973e6ad81c95804856b99446bf8f93ddecb2919583f52691056bca5cffa76",
        "HOST":"ec2-34-194-130-103.compute-1.amazonaws.com",
        "PORT":"5432"
    }     
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
    
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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en-us'

LANGUAGES = (            # supported languages
    ('en', _('English')),
    ("ar",_("Arabic")),
)
TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_L10N = True
        
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=  BASE_DIR/"static"

STATICFILES_DIRS=[
    BASE_DIR/"static_in_env"
] 

MEDIA_URL="/media/"

MEDIA_ROOT= BASE_DIR/"media"

STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
django_heroku.settings(locals())
#for translation
LOCALE_PATHS=(   
    os.path.join(BASE_DIR,"locale/"),
             )
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CkEditor
CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND ="pillow"
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_RESTRICT_BY_USER =True
CKEDITOR_BROWSE_SHOW_DIRS =False
CKEDITOR_FORCE_JPEG_COMPRESSION =True