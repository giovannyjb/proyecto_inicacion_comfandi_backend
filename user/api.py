from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
import json

from .serializers import UserTokenSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        try:

            user_serializer = self.serializer_class(data=request.data)

            if user_serializer.is_valid():

                user = User(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=make_password(request.POST['password'], 'pass', 'pbkdf2_sha256'),
                )
                user.save()

                data = {
                    "results": "user created correctly",
                    "status": "OK"

                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {
                    "errors": user_serializer.errors,
                    "status": "ERROR"
                }
                return Response(data)
        except NameError:

            return Response({"errors": NameError}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"])
    def login(self, request):
        received_json_data = json.loads(request.body)
        user_serializer = UserTokenSerializer(data=request.data)
        if user_serializer.is_valid():

            user = User.objects.filter(email=received_json_data['email'],
                                       password=make_password(received_json_data['password'], 'pass',
                                                              'pbkdf2_sha256')).first()
            if user is not None:
                token = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if token[0]:
                    return JsonResponse({
                        'token': token[0].key,
                        'user': user_serializer.data,
                        'message': 'done'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': "user no exits"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": "no valid"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
