from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    # Price in Lakhs
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    mileage = models.FloatField()

    fuel_type = models.CharField(
        max_length=50,
        default="Petrol"
    )

    purpose = models.CharField(
        max_length=50,
        default="Family"
    )

    seating_capacity = models.IntegerField(
        default=5
    )

    top_speed = models.IntegerField(
        default=180
    )

    def __str__(self):
        return self.name
    


class TestDrive(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.car.name}"