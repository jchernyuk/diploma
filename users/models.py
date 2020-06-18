from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='avatars/',
        verbose_name='Аватар'
    )
