from django.conf import settings
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

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            if instance.path:
                representation['path'] = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{instance.path}'
            return representation
