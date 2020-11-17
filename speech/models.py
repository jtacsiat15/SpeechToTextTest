from django.db import models

# Create your models here.



class Speech(models.Model):
    speech_text = models.CharField(max_length=200)