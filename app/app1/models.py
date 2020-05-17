from django.db import models

from django.contrib.auth.models import User

class kk(models.Model):
    use=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio=models.URLField(blank=True)
    display_pic=models.ImageField(upload_to='pics',blank=True)
