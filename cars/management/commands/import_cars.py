import csv

from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('cars.csv', newline='', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:

                Car.objects.create(
                    name=row['name'],
                    brand=row['brand'],
                    price=row['price'],
                    mileage=row['mileage'],
                    fuel_type=row['fuel_type'],
                    purpose=row['purpose'],
                    seating_capacity=row['seating_capacity'],
                    top_speed=row['top_speed']
                )

        self.stdout.write(
            self.style.SUCCESS('Cars imported successfully!')
        )