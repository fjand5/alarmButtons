from django.http import JsonResponse
from django.views import View
from .models import Button
from django.forms.models import model_to_dict
# Create your views here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def sendWs(data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'maintain',
        data
    )

@receiver(post_save)
def model_save(sender, **kwargs):
    data = {
                'type': 'send_message',
                'message': "message",
                "event": "MOVE",
                }
    sendWs(data)
class Buttons(View):
    def post(self, request):
        id = request.body.decode("utf-8") 
        try:
            button = Button.objects.get(id = id)
            button.status = True
            button.save()
            data = {'success':"save success"}
            model_save()
        except:
            data = {'err':"can't save"}

        response = JsonResponse(data,status=200)
        
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

    def get(self, request):
        buttons = []
        allButton = Button.objects.all()
        for button in allButton:
            buttons.append(model_to_dict(button))
        data = {'buttons':buttons}
        response = JsonResponse(data,status=200)
        
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
