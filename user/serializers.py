from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import AboutMe, Experience


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = (
            'id', 'job_description', 'experience', 'clients', 'projects', 'description', 'created_at', 'updated_at',
            'user_id', 'img_profile','cv','phone')


class AboutMeUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['user'].required = False

    class Meta:
        model = AboutMe
        fields = (
            'id', 'job_description', 'experience', 'clients', 'projects', 'description', 'created_at', 'updated_at',
            'user_id', 'img_profile', 'user','cv','phone')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'type', 'title', 'user_id','level', 'created_at', 'updated_at')


class UserAllSerializer(serializers.ModelSerializer):
    about_me = AboutMeSerializer()
    experiences = ExperienceSerializer(many=True)


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'about_me', 'experiences')
