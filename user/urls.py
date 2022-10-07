from rest_framework import routers
from user.api import UserViewSet, AboutMeViewSet, ExperienceViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('about_me', AboutMeViewSet, basename='about_me',)
router.register('experience', ExperienceViewSet, basename='experience')

urlpatterns = router.urls


