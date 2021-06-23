import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class Esp8266(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "Esp8266",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.channel_name
        )

    async def receive(self, text_data):
        try: 
            data = json.loads(text_data)
            data.update({
                'type': 'send_message',
                'message': "message",
                "event": "MOVE",
                "self.channel_name":self.channel_name
                }
            )
        except:

            data = {
                'type': 'send_message',
                'message': "can't loads json",
                "event": "ERROR"
                }
        await self.channel_layer.group_send("Esp8266",data)
    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "data": res,
        }))
    