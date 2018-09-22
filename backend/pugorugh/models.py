from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, IntegerField, OneToOneField

class Dog(Model):
    name = CharField(max_length=255)
    image_filename = CharField(max_length=255)
    breed = CharField(max_length=255)
    age = IntegerField()
    gender = CharField(max_length=255, default='u')
    size = CharField(max_length=255, default='u')

class UserDog(Model):
    user = OneToOneField(User)
    dog = OneToOneField(Dog)
    status = CharField(max_length=255)

class UserPref(Model):
    user = OneToOneField(User)
    age = CharField(max_length=255)
    gender = CharField(max_length=255)
    size = CharField(max_length=255)