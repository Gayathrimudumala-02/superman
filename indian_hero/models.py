from django.db import models

# Create your models here.
class indian(models.Model):
    name=models.CharField(max_length=50)
    weapon=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    