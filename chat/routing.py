from django.urls import re_path
import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)', consumers.CharRoomConsumer),
]



# re_path — это устаревший аналог path в Django для работы с URL-шаблонами через регулярные выражения.