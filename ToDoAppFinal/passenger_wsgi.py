# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/s/bokareab.beget.tech/hellodjango/')
sys.path.insert(1, '/home/s/bokareab.beget.tech/venv_django/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hellodjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()