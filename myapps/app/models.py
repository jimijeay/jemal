from django.db import models

#Create your models here.
class product(models.Model):
    models.TextField()
    title=models.TextField()
    description=models.TextField()
    price=models.TextField()
    summary=models.TextField(default="coooool")
