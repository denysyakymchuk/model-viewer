from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ThreeDModel


class ThreeDModelSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ThreeDModel
        fields = ['owner', 'path', 'path_skybox_image', 'path_env_image']
