from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from model_app.views import ThreeDModelViewSet

# URL configuration
router = routers.SimpleRouter()
router.register(r'models', ThreeDModelViewSet)


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
