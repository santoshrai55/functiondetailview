from pydoc import describe
from django.db import models

# Create your models here.


class Gharkhet(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="gharkhet_app/images")
    price = models.IntegerField()
