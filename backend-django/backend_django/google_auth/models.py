from django.db import models

class EmailAddress(models.Model):
    email = models.EmailField()
    verified = models.BooleanField(default=False)

    class Meta:
        unique_together = (('email', 'verified'),)
