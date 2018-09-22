from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    age = CharField(max_length=255, default="b,y,a,s")
    gender = CharField(max_length=255, default="f,m")
    size = CharField(max_length=255, default="s,m,l,xl")

@receiver(post_save, sender=User)
def create_user_pref(sender, instance, created, **kwargs):
    """Creates a user pref when a user is created"""
    if created:
        UserPref.objects.create(user=instance).save()