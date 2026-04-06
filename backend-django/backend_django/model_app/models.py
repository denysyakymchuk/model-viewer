from django.db import models
from django.conf import settings

class ThreeDModel(models.Model):
    path = models.FileField(upload_to='3d_models/', null=False)
    path_skybox_image = models.FileField(upload_to='skybox_images/', null=True)
    path_env_image = models.FileField(upload_to='env_images/', null=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return f'{self.path}'

    class Meta:
        verbose_name = "ThreeDModel"
        verbose_name_plural = "ThreeDModels"
        ordering = ("-time_create",)


class ThreeDModelHistoryOwner(models.Model):
    id = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)