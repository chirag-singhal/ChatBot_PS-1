from django.contrib.auth.models import User                               
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from queries.serializers import  query1Serializer # Our Serializer Classes
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
@csrf_exempt                         
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'POST':
        body = {"message": "hi from backend"}
        return JsonResponse(body, status=200)