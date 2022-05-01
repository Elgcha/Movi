"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from server.settings import STATIC_URL
from socketio_app.views import sio
import socketio
import eventlet
import eventlet.wsgi


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)
eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), application)
