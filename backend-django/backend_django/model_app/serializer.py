from rest_framework import serializers
from .models import ThreeDModel


class ThreeDModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeDModel
        fields = ['id', 'path', 'path_skybox_image', 'path_env_image', 'time_create', 'time_update', 'owner']

        def validate(self, data):
            # If 'path_skybox_image' is not provided, set it to None
            if 'path_skybox_image' not in data:
                data['path_skybox_image'] = None

            # If 'path_env_image' is not provided, set it to None
            if 'path_env_image' not in data:
                data['path_env_image'] = None

            return data