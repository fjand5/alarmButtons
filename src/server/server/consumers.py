import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from alarmButtons.models import Button, History
from channels.db import database_sync_to_async


async def addToHistory(macAddr, buttonNum, status):
    obj = await database_sync_to_async(History)(macAddr=macAddr, buttonNum=buttonNum, status = status)
    await database_sync_to_async(obj.save)()

async def creteOrUpdateButton(macAddr, buttonNum, status):
    try:
        obj = await database_sync_to_async(Button.objects.get)(macAddr=macAddr, buttonNum=buttonNum)
        obj.status = status

    except Button.DoesNotExist:
        obj = await database_sync_to_async(Button)(macAddr=macAddr, buttonNum=buttonNum, status = status)
    await database_sync_to_async(obj.save)()
    
    await addToHistory(macAddr, buttonNum, status) 
class Esp8266(AsyncJsonWebsocketConsumer):
    async def connect(self):
        client = self.scope['url_route']['kwargs']['client']
        await self.channel_layer.group_add(
            client,
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
                "event": "ALARM",
                "self.channel_name":self.channel_name
                }
            )
            macAddr = data["macAddr"]
            buttonNum = data["buttonNum"]
            status = data["status"]
            await creteOrUpdateButton(macAddr,buttonNum,status)
        except:
            data = {
                'type': 'send_message',
                'message': "can't loads json",
                "event": "ERROR"
                }
        await self.channel_layer.group_send("maintain",data)
    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "data": res,
        }))
    