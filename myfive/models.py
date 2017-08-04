from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    # Add country
    # Add created_at


    def __str__(self):
        return self.name
