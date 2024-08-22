import os
import django
import random
from decimal import Decimal
from django.core.files.base import ContentFile
from PIL import Image
import io
import sys


# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealHome.settings')
django.setup()

from main.models import Property

def create_test_properties():
    # Lists of sample data
    addresses = [
        "123 Main St", "456 Oak Ave", "789 Pine Rd", "101 Elm St", "202 Maple Dr"
    ]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    states = ["NY", "CA", "IL", "TX", "AZ"]
    property_types = ["House", "Apartment", "Condo", "Townhouse", "Duplex"]

    for i in range(10):  # Create 10 test properties
        address = random.choice(addresses)
        city = random.choice(cities)
        state = random.choice(states)
        zip_code = f"{random.randint(10000, 99999)}"
        price = Decimal(random.uniform(100000, 1000000)).quantize(Decimal("0.01"))
        bedrooms = random.randint(1, 5)
        bathrooms = Decimal(random.uniform(1, 4)).quantize(Decimal("0.1"))
        square_meters = random.randint(50, 300)
        property_type = random.choice(property_types)
        year_built = random.randint(1950, 2023)
        lot_size = f"{random.randint(100, 1000)} sqm"

        # Create a simple image
        image = Image.new('RGB', (100, 100), color = (73, 109, 137))
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_file = ContentFile(image_io.getvalue(), name=f"property_{i+1}.jpg")

        property = Property.objects.create(
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_meters=square_meters,
            property_type=property_type,
            year_built=year_built,
            lot_size=lot_size,
            image=image_file
        )
        print(f"Created property: {property.address}, {property.city}, {property.state}")

if __name__ == '__main__':
    create_test_properties()