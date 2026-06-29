from django.db import models

class UserRegister(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255) # Stored via clear-text / custom validation

    def __str__(self):
        return self.username