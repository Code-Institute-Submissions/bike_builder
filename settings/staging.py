from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_kLdDMq39gQJuwVRHNbtROldY')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_sNgcHOXBxiaZuVTDDAnX2AIQ')
