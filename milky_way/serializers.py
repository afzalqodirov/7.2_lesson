from .models import Star
from rest_framework import serializers


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

class StarSerializerOther(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ['id','name']
