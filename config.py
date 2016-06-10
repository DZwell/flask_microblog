import os
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY')

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}
]
