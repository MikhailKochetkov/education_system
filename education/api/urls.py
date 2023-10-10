from django.urls import include, path
from rest_framework import routers

from .views import LessonViewSet, LessonsByProductViewSet, ProductStatisticViewSet


router = routers.DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('v1/statistic/', ProductStatisticViewSet.as_view({'get': 'list'})),
    path('v1/product/<int:product_id>/lessons/', LessonsByProductViewSet.as_view({'get': 'list'})),
    path('v1/', include(router.urls)),
]
