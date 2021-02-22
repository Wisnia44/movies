from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=80)
	year = models.CharField(max_length=4)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
