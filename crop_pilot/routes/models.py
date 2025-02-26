from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_depot = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Machine(models.Model):
    name = models.CharField(max_length=100)
    capacity_kg = models.FloatField()  
    speed_kmh = models.FloatField()   
    fuel_consumption_lh = models.FloatField()
    operation_type = models.CharField(max_length=50, choices=[('harvest', 'Colheita'), ('transport', 'Transporte')])

    def __str__(self):
        return self.name