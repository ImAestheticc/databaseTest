from django.db import models

# Create your models here.
class userModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
