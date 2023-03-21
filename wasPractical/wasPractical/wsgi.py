"""
WSGI config for wasPractical project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
path = os.path.expanduser('~/wasPractical')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'wasPractical.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
