import csv

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from foodtrucks.models import FoodTruck


class Command(BaseCommand):
    help = "Load data from a CSV file into the FoodTruck model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]

        with open(csv_file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row

            for row in csv_reader:
                try:
                    # Validate latitude and longitude
                    latitude = float(row[14])
                    longitude = float(row[15])
                    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
                        raise ValidationError("Invalid latitude or longitude")

                    # Check for existing record with the same coordinates
                    if FoodTruck.objects.filter(
                        Latitude=latitude, Longitude=longitude
                    ).exists():
                        self.stdout.write(
                            self.style.WARNING(
                                f"Duplicate coordinates found: {latitude}, {longitude}"
                            )
                        )
                        continue  # Skip creating a new record

                    # Create FoodTruck object
                    FoodTruck.objects.create(
                        locationid=row[0],
                        Applicant=row[1],
                        Address=row[5],
                        Latitude=latitude,
                        Longitude=longitude,
                    )
                except (ValueError, ValidationError, IntegrityError) as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error processing row: {row}, {e}")
                    )

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
