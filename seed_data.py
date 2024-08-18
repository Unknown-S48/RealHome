import os
import django
import random
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealHome.settings')
django.setup()

from main.models import Property

def create_test_properties():
    # List of sample property titles
    titles = [
        "Cozy Downtown Apartment",
        "Spacious Suburban House",
        "Modern City Loft",
        "Rustic Country Cottage",
        "Luxury Beachfront Villa"
    ]

    # List of sample descriptions
    descriptions = [
        "A beautiful property with modern amenities.",
        "Perfect for families, close to schools and parks.",
        "Stunning views of the city skyline.",
        "Escape to nature in this charming home.",
        "Experience luxury living by the sea."
    ]

    # List of sample addresses
    addresses = [
        "123 Main St, Anytown, USA",
        "456 Oak Ave, Somewhere, USA",
        "789 High St, Metropolis, USA",
        "101 Country Rd, Rural, USA",
        "202 Beach Blvd, Coastal, USA"
    ]

    for i in range(6):  # Create 10 test properties
        title = random.choice(titles)
        description = random.choice(descriptions)
        price = round(random.uniform(100000, 1000000), 2)
        address = random.choice(addresses)

        property = Property.objects.create(
            title=title,
            description=description,
            price=price,
            address=address
        )
        print(f"Created property: {property.title}")

if __name__ == '__main__':
    create_test_properties()