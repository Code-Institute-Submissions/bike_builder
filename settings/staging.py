from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.parse(os.getenv('CLEARDB_DATABASE_URL'))
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_kLdDMq39gQJuwVRHNbtROldY')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_sNgcHOXBxiaZuVTDDAnX2AIQ')
