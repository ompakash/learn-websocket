from django.urls import path
from .consumers import *

websocket_patterns=[
    path('ws/sc/', MySyncConsumer.as_asgi()),
    path('ws/ac/', MyAsyncConsumer.as_asgi()),
]