from django.contrib.auth.models import User                               
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from queries.serializers import  query1Serializer # Our Serializer Classes
from rest_framework.decorators import api_view
from nlp_module import respond
import response_generation
import json

@api_view(['GET', 'POST'])
@csrf_exempt                         
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'POST':
        var=json.dumps(request)
        input_question=var["messages"]
        nlp_out.respond(input_question)
        final_out = response_generation(nlp_out)
        body = {"message": final_out}
        return JsonResponse(body, status=200)
