from django.db import models

# TODO: crear los modelos para la base de datos

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ": " + self.username

class File(models.Model):
    name = models.CharField(max_length=100)
    path = models.TextField()

    def __str__(self):
        return self.name
