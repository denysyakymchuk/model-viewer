from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from model_app.views import ThreeDModelViewSet


# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL configuration
router = routers.SimpleRouter()
router.register(r'models', ThreeDModelViewSet)


urlpatterns = [
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
