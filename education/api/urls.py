from django.urls import include, path
from rest_framework import routers

from .views import LessonViewSet


router = routers.DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('v1/', include(router.urls)),
]
