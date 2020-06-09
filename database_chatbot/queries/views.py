from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Query
from .serializers import query1Serializer

class Post_query2_List(APIView):
    @classmethod
    def get_extra_actions(cls):
        return []
    def post(self, request, fomrat = None):
        serializer = query1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
        
def homepage(request):
    return render(request, 'index.html')


# Create your views here.
