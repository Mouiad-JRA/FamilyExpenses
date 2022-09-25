
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_w7$ih&fr7xpkfm!qh7ka4@joc_b#9!%56x5%^)-yg%mylhg#!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  'db.sqlite3',
    }
}


