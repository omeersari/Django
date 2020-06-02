from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save


class Duyuru(models.Model):
    duyurular_title = models.CharField(max_length = 200)
    duyurular_content = models.TextField()
    duyurular_published = models.DateTimeField("Yayınlandığı Tarih", default=timezone.now())

    class Meta:
        verbose_name_plural = "Duyurular"
    
    def __str__(self):
        return self.duyurular_title

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    login_last = models.DateTimeField(blank=True, default=timezone.now())
    login_count = models.CharField(max_length=200,blank=True, default="")

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
 
    def __str__(self):
        return self.user.username




def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)