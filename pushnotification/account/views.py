from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

import firebase_admin
from firebase_admin import credentials, messaging


fcred = credentials.Certificate("C:/Users/ADMIN/Downloads/PushNotification/pushnotification/pushnotification/serviceAccountKey.json")
firebase_admin.initialize_app(fcred)

# Create your views here.
@api_view(['POST',])
def sendNotification(request):
    if request.method == "POST":
        title = request.POST['title']
        msg = request.POST['msg']
        
        tokens = ["dE9BDRuKRJa31AmN6GoapE:APA91bE5vZzxt8_-o_iCRZlSWlrP4CX-TE635DCkAsu5guvYnUXVRFLl-S6Ek2GPfTcx-GqKAJKHi4vt1S3xuF2GFXtXZAxZO9B2aSiqa4gSaHwgh4NsO7cqO5HvxAH4K_JR8SZYY37y","fjheUNuJS2W27sgO6j6nn3:APA91bFQu4jWYa1Z4kvDtiVtpmY_dtMUm3EsE2WL88hEiRTmThdiJamdlQO-_bwcPPo7Iov9NZR_aYENczOo-iHlPWyHE-_qLinpqQPJBqXNX71cCgNUsCOt27Zm60-hg4cxCbVqLdqq"]

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=msg
            ),
            data=None,
            tokens=tokens,
        )

        response = messaging.send_multicast(message)

        # response=json.dumps(response)

        responsesss = {
                        'status':200,
                        'message': "success",
                        }

        # main_result=json.dumps(results)
        return JsonResponse(responsesss,safe=False)