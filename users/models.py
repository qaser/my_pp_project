from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone


class Role(models.TextChoices):
    MANAGER = 'начальник'
    ENGENEER = 'инженер'
    MACHINIST = 'машинист'
    GUEST = 'гость'


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=60,
        unique=True,
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    # role = models.CharField(
    #     max_length=30,
    #     choices=Role.choices,
    #     default=Role.GUEST
    # )
    password = models.CharField(max_length=20)
