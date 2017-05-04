from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Role(models.Model):
    RoleName = models.CharField(max_length  = 255)


    def __str__(self):
         return self.RoleName

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roleid = models.IntegerField(default = 3)
@receiver(post_save, sender=User)
def set_user(sender,instance,created,**kwargs):
    if created:
        UserRole.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_set(sender,instance,**kwargs):
    instance.userrole.save()


    def __str__(self):
         return self.RoleName

class Partners(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length  = 255)
    CompanyEmail = models.EmailField(max_length  = 254)
    HQAddress = models.CharField(max_length  = 255)
    class Meta:
        verbose_name_plural = 'Partners'

    def __str__(self):
         return self.CompanyName
