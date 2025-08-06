from django.ab.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models imoport Profile

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,craeted, **kwargs):
    if created:
        Profile.object.create(user=instance)
        @receiver(post_save, sender=User)
        def save_user_profile(sender,instance,**kwargs):
            instance.profile.save()