
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password','status','created_at','updated_at')
        read_only_fields = ('created_at',)
        hash = ('password')
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            password = make_password(validated_data['password']),
            status = 0,
            )

        user.save()
        return user
 
            