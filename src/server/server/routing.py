from django.conf.urls import url
from server.consumers import Esp8266

websocket_urlpatterns = [
    url(r'^ws/$', Esp8266.as_asgi()),
]