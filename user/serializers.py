from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'status', 'created_at', 'updated_at')
        read_only_fields = ('created_at',)


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
