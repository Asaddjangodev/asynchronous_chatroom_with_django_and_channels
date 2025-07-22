from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat import routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})



# ProtocolTypeRouter - Главный маршрутизатор, который определяет:
# Как обрабатывать разные типы соединений (HTTP, WebSocket, и др.)

# AuthMiddlewareStack - Мидлварь для:
# Аутентификации WebSocket-соединений
# Доступа к пользователю через self.scope["user"]
# Работает аналогично Django's Session/Auth middleware
#
# URLRouter - Роутер URL для:
# Маршрутизации WebSocket-запросов по аналогии с Django URL
# Подключения consumer'ов к конкретным путям