from rest_framework import serializers
from .models import Query

class query1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
        