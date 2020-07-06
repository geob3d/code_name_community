from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    zipcode = models.IntegerField(db_column='zipCode',null=True, blank=True)  # Field name made lowercase.

    REQUIRED_FIELDS = ['zipcode','email'] # this will determine the required user fields to enter