from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustUser(AbstractUser):
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    options=(
        ("store","store"),
        ("customer","customer"),
    )
    usertype=models.CharField(max_length=100,choices=options,default="customer")

