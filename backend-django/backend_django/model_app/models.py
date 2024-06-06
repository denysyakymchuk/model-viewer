from django.contrib.auth.models import User
from django.db import models


class ThreeDModel(models.Model):
    path = models.CharField(max_length=100)
    path_skybox_image = models.CharField(max_length=100)
    path_env_image = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return f'{self.path}'

    class Meta:
        verbose_name = "ThreeDModel"
        verbose_name_plural = "ThreeDModels"
        ordering = ("-time_create",)

