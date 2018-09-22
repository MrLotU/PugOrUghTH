from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, OneToOneField, ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver

class Dog(Model):
    name = CharField(max_length=255)
    image_filename = CharField(max_length=255)
    breed = CharField(max_length=255)
    age = IntegerField()
    gender = CharField(max_length=255, default='u')
    size = CharField(max_length=255, default='u')
    age_classification = CharField(max_length=255, default='u')
    
    def save(self, *args, **kwargs):
        if self.age < 12:
            self.age_classification = 'b'
        elif self.age <= 24:
            self.age_classification = 'y'
        elif self.age <= 72:
            self.age_classification = 'a'
        else:
            self.age_classification = 's'
        super(Dog, self).save(*args, **kwargs)

class UserDog(Model):
    user = ForeignKey(User)
    dog = ForeignKey(Dog)
    status = CharField(max_length=255, default='u')

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
        for dog in Dog.objects.all():
            UserDog.objects.create(user=instance, dog=dog).save()