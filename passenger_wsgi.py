# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1546242/data/www/server-learn-qa.ru/blog')
sys.path.insert(1, '/var/www/u1546242/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()