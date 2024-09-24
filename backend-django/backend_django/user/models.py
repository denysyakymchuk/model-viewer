from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True #make user field email unique
