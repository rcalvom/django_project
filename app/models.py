from django.db import models

# TODO: crear los modelos para la base de datos

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ": " + self.username

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/', max_length=200, default=None)

    def __str__(self):
        return self.name
