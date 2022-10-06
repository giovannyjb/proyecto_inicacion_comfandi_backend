from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import AboutMe, Experience


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
        fields = ('email', 'password')


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('id', 'experience', 'clients', 'projects', 'description', 'created_at', 'updated_at', 'user_id')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'type', 'title', 'user_id', 'created_at', 'updated_at')
