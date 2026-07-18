from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    mileage = models.FloatField()
    fuel_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TestDrive(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    date = models.DateField()
    def __str__(self):      return f"{self.name} - {self.car.name}"

