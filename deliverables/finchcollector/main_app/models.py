from django.db import models
from django.urls import reverse

from datetime import date

# Create your models here.

  

  
class Finch(models.Model):
  species = models.CharField(max_length=100)
  diet = models.CharField(max_length=100)
  lifespan = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  unique_characteristics = models.CharField(max_length=250)
  
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(Feeding.MEALS)
  
  def __str__(self) -> str:
    return self.species
  
  def get_absolute_url(self):
    return reverse('details', kwargs={'finch_id': self.id})
  
class Feeding(models.Model):
  MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
  )
  date = models.DateField('Feeding Date')
  meal = models.CharField(max_length=1,
  choices=MEALS,
  default=MEALS[0][0],
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
    
    
