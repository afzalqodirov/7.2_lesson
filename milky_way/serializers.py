from .models import Star
from rest_framework import serializers
from django.contrib.auth.models import User


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields =['name', 'description', 'image']
        read_only_fields = ['views_count']

class StarSerializerOther(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ['id','name', 'image']

class StarAll(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'
        read_only_fields = ['views_count', 'user']

class Seria(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True, style = {'input_type':'password'})
    confirm_password = serializers.CharField(write_only = True, required = True, label='Confirm password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'is_staff']
        read_only_fields = ['is_staff']

    def validate(self, atribs):
        if atribs['password'] != atribs['confirm_password']:
            raise serializers.ValidationError({'password':'Passwords didn\'t match'})
        return atribs

    def create(self, data):
        data.pop('confirm_password')
        user = User.objects.create_user(**data)
        return user

class ChangePassSeria(serializers.Serializer):
    old_pass = serializers.CharField(required=True)
    new_pass = serializers.CharField(required=True)

    class Meta:
        fields = ['old_pass', 'new_pass']
