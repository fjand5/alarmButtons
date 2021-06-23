from django.conf.urls import url
from server.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    url(r'^ws/$', TicTacToeConsumer.as_asgi()),
]