from django.db import models
from django.urls import reverse

# Create your models here.


class Workers(models.Model):

    name= models.CharField( max_length=50)
    phone = models.CharField( max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class Unit(models.Model):
    name = models.CharField( max_length=50)
    worker = models.ForeignKey(Workers,on_delete=models.CASCADE)
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Visit(models.Model):
    time_of_visit = models.DateTimeField( auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField() 
        

    def __str__(self):
        return f'Visit {self.pk}'

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
