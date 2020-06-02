from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    area=models.CharField(max_length=100,null = True)
    malaria=models.BooleanField(default=False)
    dengue=models.BooleanField(default=False)
    aids=models.BooleanField(default=False)
    cancer=models.BooleanField(default=False)
    corona=models.BooleanField(default=False)
    polio=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username