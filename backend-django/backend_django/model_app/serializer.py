from rest_framework import serializers

from .models import ThreeDModel
from user.serializer import UserSerializer

class ThreeDModelSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_details = UserSerializer(source='owner', read_only=True)

    class Meta:
        model = ThreeDModel
        fields = ['id', 'path', 'path_skybox_image', 'is_active', 'path_env_image', 'time_create', 'time_update', 'owner', 'owner_details']
        read_only_fields = ['owner_details']

    def validate_path(self, path):
        if str(path).split('.')[-1] != 'glb':
            raise serializers.ValidationError('No valid file format. Must be glb.')
        return path

    def validate_path_skybox_image(self, path_skybox_image):
        if str(path_skybox_image).split('.')[-1] != 'jpg' and str(path_skybox_image).split('.')[-1] != 'hdr' and str(path_skybox_image) != 'None':
            raise serializers.ValidationError('No valid file format. Must be jpg or hdr.')
        return path_skybox_image

    def validate_path_env_image(self, path_env_image):
        if str(path_env_image).split('.')[-1] != 'jpg' and str(path_env_image) != 'None':
            raise serializers.ValidationError('No valid file format. Must be jpg.')
        return path_env_image
