import json

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AboutMe, Experience
from .serializers import UserTokenSerializer, UserSerializer, AboutMeUserSerializer, ExperienceSerializer, \
    UserAllSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        try:
            received_json_data = json.loads(request.body)
            user_serializer = self.serializer_class(data=request.data)

            if user_serializer.is_valid():

                user = User(
                    username=received_json_data['username'],
                    email=received_json_data['email'],
                    first_name=received_json_data['first_name'],
                    last_name=received_json_data['last_name'],
                    password=make_password(received_json_data['password'], 'pass', 'pbkdf2_sha256'),
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
                return Response(data, status.HTTP_200_OK)
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

    @action(detail=False, methods=["GET"], permission_classes=[permissions.IsAuthenticated])
    def find_all(self, request):
        queryset = User.objects.get(id=request.GET['id'])
        serializer = UserAllSerializer(queryset, many=False)

        return Response(serializer.data)

    @action(detail=False, methods=["POST"], permission_classes=[permissions.IsAuthenticated])
    def load_data(self, request):
        file = request.FILES.get('file').read()
        # attachment = open(file, mode="r")
        # open(file=file, mode="r", encoding = 'utf8')
        # os.mkdir('probando')
        # shutil.move(file, 'probando/test.txt')
        # os.open(file,flags=os.O_RDWR)
        # os.close(file)
        list_data = list(str(file).split(','))

        first_name = list_data[0].split(':')[1]
        last_name = list_data[1].split(':')[1]

        user = User(first_name=first_name, last_name=last_name)
        user.save()

        phone = list_data[2].split(':')[1]
        job_description = list_data[3].split(':')[1]
        description = list_data[4].split(':')[1]
        experience = list_data[5].split(':')[1]
        clients = list_data[6].split(':')[1]
        projects = list_data[7].split(':')[1]

        about_me = AboutMe(
            img_profile=request.FILES.get('img'),
            cv=request.FILES.get('cv'),
            phone=phone, job_description=job_description,
            description=description, experience=experience,
            clients=clients, projects=projects, user_id=user.id)
        about_me.save()

        frontend = (list_data[8].split(':')[1]).split('/')

        for element in frontend:
            data = element.split('-')
            experience = Experience(type=0, title=data[0], level=data[1], user_id=user.id)
            experience.save()

        backend = (list_data[9].split(':')[1]).split('/')
        for element in backend:
            data = element.split('-')
            experience = Experience(type=1, title=data[0], level=data[1], user_id=user.id)
            experience.save()

        return Response({"results": "user created"})


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AboutMeUserSerializer

    def create(self, request, *args, **kwargs):
        # received_json_data = json.loads(request.body)
        about_me_serializer = self.serializer_class(data=request.data)

        if about_me_serializer.is_valid() and request.POST:
            about_me = AboutMe(
                user_id=request.POST.get('user_id'),
                phone=request.POST.get('phone'),
                job_description=request.POST.get('job_description'),
                experience=request.POST.get('experience'),
                clients=request.POST.get('clients'),
                projects=request.POST.get('projects'),
                description=request.POST.get('description'),
                img_profile=request.FILES.get('img_profile'),
                cv=request.FILES.get('cv')
            )

            about_me.save()

            data = {
                "results": "about_me created correctly",
                "status": "OK"

            }
            return Response(data, status=status.HTTP_200_OK)

        else:
            data = {
                "errors": about_me_serializer.errors,
                "status": "ERROR"
            }
            return Response(data, status.HTTP_200_OK)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExperienceSerializer

    def create(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body)
        experience_serializer = self.serializer_class(data=request.data)

        if experience_serializer.is_valid():
            experience = Experience(
                user_id=received_json_data['user_id'],
                level=received_json_data['level'],
                type=received_json_data['type'],
                title=received_json_data['title'],
            )

            experience.save()

            data = {
                "results": "experience created correctly",
                "status": "OK"

            }
            return Response(data, status=status.HTTP_200_OK)

        else:
            data = {
                "errors": experience_serializer.errors,
                "status": "ERROR"
            }
            return Response(data, status.HTTP_200_OK)
