
import json
from channels.generic.websocket import AsyncWebSockerConsumer
# Импорт базового класса для асинхронного WebSocket-чата

# Создаем класс чат-комнаты (наследуемся от базового класса)
class ChatRoomConsumer(AsyncWebSocketConsumer):
    # Метод, который срабатывает при подключении нового пользователя
    async def connect(self):
        # 1. Достаем название комнаты из URL (например, из ws/chat/lobby/)
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # 2. Создаем уникальное имя группы для этой комнаты (chat_lobby)
        self.room_group_name = 'chat_%s' % self.room_name

        # 3. Добавляем текущее соединение в группу комнаты
        # (чтобы потом можно было рассылать сообщения всем в этой комнате)
        await self.channel_layer.group_add(
            self.room_group_name,  # Имя группы (chat_lobby)
            self.channel_name # Уникальный ID этого соединения
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'hello world',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_date=json.dumps({
            'tester': tester,
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.groud_discard(
            self.room_group_name,
            self.channel_name
        )

        pass
