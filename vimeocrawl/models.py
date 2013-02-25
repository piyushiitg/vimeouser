from django.db import models

# Create your models here.
class Vimeouserinfo(models.Model):
    Name = models.CharField(max_length=255)
    URL = models.CharField(max_length=255,primary_key=True)
    Paying = models.CharField(max_length=3)
    StaffPick = models.CharField(max_length=3)
    Video = models.CharField(max_length=3)

