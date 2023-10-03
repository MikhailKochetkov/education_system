from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', basename='likes')

urlpatterns = [
    path('v1/', include(router.urls)),
]
