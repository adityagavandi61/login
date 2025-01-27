from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilepic = models.FileField(upload_to='profile_images', null=True,blank=True)

    def __str__(self):
        return self.user.username

