import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from users.models import Customer
from .models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(True)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    
    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    

    def receive(self, text_data=None, bytes_data=None):
         # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        is_agent = text_data_json['is_agent']
        if not is_agent:
            user_obj = Customer.objects.get(user__username=username)
            message_obj = Message(
                value = message,
                customer = user_obj
            )
            message_obj.save()
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username':username,
                'is_agent': is_agent,
            }
        )
        print(True, 'Message added')

    def chat_message(self, event):
        # Receive message from room group
        message = event['message']
        username = event['username']
        is_agent = event['is_agent']
        print(message)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'is_agent': is_agent,
        }))
        print(True, 'Message send')