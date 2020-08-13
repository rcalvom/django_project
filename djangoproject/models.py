from django.db import models

# TODO: crear los modelos para la base de datos

class User(models.Model):
    username = models.CharField(maxlength=20)
    password = models.CharField(maxlength=20)
