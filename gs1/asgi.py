"""
ASGI config for gs1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app.routing import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs1.settings')

application = get_asgi_application()

application  = ProtocolTypeRouter({
    "http" : application,
    "websocket" : URLRouter(websocket_patterns)
})
