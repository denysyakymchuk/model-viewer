from django.contrib.auth.models import User
from django.db import models


class ThreeDModel(models.Model):
    path = models.FileField(upload_to='3d_models/', null=False)
    path_skybox_image = models.FileField(upload_to='skybox_images/', null=True)
    path_env_image = models.FileField(upload_to='env_images/', null=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return f'{self.path}'

    class Meta:
        verbose_name = "ThreeDModel"
        verbose_name_plural = "ThreeDModels"
        ordering = ("-time_create",)
