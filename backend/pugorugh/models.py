from django.contrib.auth.models import User
from django.db.models import (CharField, ForeignKey, IntegerField, Model,
                              OneToOneField, CASCADE)
from django.db.models.signals import post_save
from django.dispatch import receiver


class Dog(Model):
    """Holds a Dog in the DB"""
    name = CharField(max_length=255)
    image_filename = CharField(max_length=255)
    breed = CharField(max_length=255, default='Unknown breed')
    age = IntegerField()
    gender = CharField(max_length=255, default='u')
    size = CharField(max_length=255, default='u')
    age_classification = CharField(max_length=255, default='u')
    
    def save(self, *args, **kwargs):
        """Saves the model"""

        # This sets the age_classification based on age in months
        # For easy comparison with the UserPref model
        if self.age < 12:
            self.age_classification = 'b'
        elif self.age <= 24:
            self.age_classification = 'y'
        elif self.age <= 72:
            self.age_classification = 'a'
        else:
            self.age_classification = 's'
        super(Dog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class UserDog(Model):
    """Releation between a dog and a user"""
    user = ForeignKey(User, on_delete=CASCADE)
    dog = ForeignKey(Dog, on_delete=CASCADE)
    status = CharField(max_length=255, default='u')

class UserPref(Model):
    """User preferences"""
    user = OneToOneField(User, on_delete=CASCADE)
    age = CharField(max_length=255, default="b,y,a,s")
    gender = CharField(max_length=255, default="f,m")
    size = CharField(max_length=255, default="s,m,l,xl")

@receiver(post_save, sender=User)
def create_user_pref(sender, instance, created, **kwargs):
    """Creates a user pref when a user is created"""
    if created:
        UserPref.objects.create(user=instance).save()
        for dog in Dog.objects.all():
            UserDog.objects.create(user=instance, dog=dog).save()