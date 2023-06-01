from django.db import models

# Create your models here.
class Finch(models.Model):
  species = models.CharField(max_length=100)
  diet = models.CharField(max_length=100)
  lifespan = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  unique_characteristics = models.CharField(max_length=250)
  
  def __str__(self) -> str:
    return self.species