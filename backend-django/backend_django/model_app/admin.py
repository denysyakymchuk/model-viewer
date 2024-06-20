from django.contrib import admin

from .models import ThreeDModel


@admin.register(ThreeDModel)
class ThreeDModelSystemAdmin(admin.ModelAdmin):
    list_display = ("path", "owner", 'path_skybox_image', 'path_env_image',  "time_create", "time_update")
