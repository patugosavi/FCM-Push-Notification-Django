from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.

#user Model
class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    CUSTOMER = 3
    ROLE_CHOICES = (
      (SUPER_ADMIN,'Super Admin'),
      (ADMIN,'Admin'),
      (CUSTOMER,'Customer'),
    )
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICE = (
        (MALE,'Male'),
        (FEMALE,'Female'),
        (OTHER,'Other'))
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=CUSTOMER)
    mobile_no = models.CharField(max_length=100,blank=True)
    otp = models.IntegerField(default=0)
    varify_status = models.BooleanField(default=False)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICE,default=MALE)
    Updated_on = models.DateTimeField(auto_now=True)