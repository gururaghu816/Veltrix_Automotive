from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # in Lakhs
    mileage = models.FloatField()
    fuel_type = models.CharField(max_length=50, default="Petrol")
    purpose = models.CharField(max_length=50, default="Family")
    seating_capacity = models.IntegerField(default=5)
    top_speed = models.IntegerField(default=180)

    # Handover-slip fields
    vin = models.CharField(max_length=20, blank=True, default="")
    plate_number = models.CharField(max_length=20, blank=True, default="")
    color = models.CharField(max_length=40, blank=True, default="")
    odometer = models.IntegerField(default=0)         # km
    fuel_level = models.IntegerField(default=100)      # percent

    # Recommend-page photo
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.name


class TestDrive(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    # Normal cars from the database
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Featured Models such as V8 Phantom
    featured_model = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    date = models.DateField()

    time_slot = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    advisor = models.CharField(
        max_length=50,
        blank=True,
        default="Veltrix Team"
    )

    signed = models.BooleanField(default=False)

    signature = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self):
        if self.featured_model:
            return f"{self.name} - {self.featured_model}"

        if self.car:
            return f"{self.name} - {self.car.name}"

        return self.name