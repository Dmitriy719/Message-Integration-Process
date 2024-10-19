import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import EmailAccount, EmailMessage
import asyncio

class EmailConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Здесь можно добавить логику для получения логина и пароля

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        email_account = EmailAccount.objects.get(id=data['account_id'])
        await self.fetch_emails(email_account)

    async def fetch_emails(self, email_account):
        # Здесь должна быть логика для подключения к почте и получения сообщений
        # Пример: используем asyncio для имитации долгого процесса
        total_messages = 100  # Примерное количество сообщений
        for i in range(total_messages):
            await asyncio.sleep(0.1)  # Имитация задержки
            progress = (i + 1) / total_messages * 100
            await self.send(text_data=json.dumps({
                'type': 'progress',
                'progress': progress,
                'message': f'Проверено {i + 1} из {total_messages} сообщений'
            }))
            # Здесь добавьте логику для получения и сохранения сообщений
            # Пример:
            message = EmailMessage(
                subject=f'Тема {i + 1}',
                sent_date='2023-01-01 12:00:
