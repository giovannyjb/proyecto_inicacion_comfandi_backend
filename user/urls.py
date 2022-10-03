from rest_framework import routers
from user.api import UserViewSet


router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls

