from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    stu_y = (
        (1, 'First'),
        (2, 'sdf'),
        (3, 'Fifsdfrst'),
        (4, 'Fisfddsfrst'),)

    year = models.IntegerField(choices=stu_y, null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
