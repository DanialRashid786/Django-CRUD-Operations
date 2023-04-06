import os
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save
from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    profileimage = models.ImageField(upload_to='employee/',max_length=200)
    

    
    def __str__(self):
        return self.name
    
@receiver(pre_delete, sender=registration)    
def delete_image(sender, instance, **kwargs):
    # Remove file from the storage
    if instance.profileimage:
        if os.path.isfile(instance.profileimage.path):
            os.remove(instance.profileimage.path)    




@receiver(pre_save, sender=registration)
def delete_previous_image(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = registration.objects.get(pk=instance.pk).profileimage
    except registration.DoesNotExist:
        return False

    new_image = instance.profileimage
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)