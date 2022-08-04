from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class RegisterForm(models.Model):
    name = CharField(max_length=64)
    rollno = IntegerField()