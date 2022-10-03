from django.http import JsonResponse
from .models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserTokenSerializer


# Create your views here.

# token

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserTokenSerializer(user)
            if created:
                return JsonResponse({
                    'token': token,
                    'user': user_serializer.data,
                    'message': 'done'})

        else:
            return JsonResponse({"HPT"})
