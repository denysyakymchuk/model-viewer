class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_admin_models_queryset(self):
        return super().get_queryset().filter(owner=get_current_user())
