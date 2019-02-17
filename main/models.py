from django.contrib.auth.models import User,AbstractUser
from django.db import models

from oauth2client.contrib.django_util.models import CredentialsField


class User(AbstractUser):
	phone = models.BigIntegerField(null=True)
	def __str__(self):
		return self.username

