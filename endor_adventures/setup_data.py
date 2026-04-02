import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'endor_park.settings')
django.setup()

from django.contrib.auth.models import User
from fastpass.models import ThemeZone, Attraction, Guest, TimeSlot
from datetime import time

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@endor.com', 'admin123')

# Data to populate
zones = [
    {"name": "Forest of Endor", "description": "Towering redwoods and ancient trees. Home to treehouse attractions."},
    {"name": "Ewok Village", "description": "The heart of Ewok civilization! Family-friendly rides."},
    {"name": "Imperial Ruins", "description": "Remnants of the fallen Empire. Thrill rides ahead!"},
    {"name": "Speeder Bike Canyon", "description": "High-speed adventures through narrow forest paths."},
    {"name": "Bright Tree Grove", "description": "Entertainment and dining district. Live shows!"},
]

for z in zones:
    ThemeZone.objects.get_or_create(name=z['name'], defaults={'description': z['description']})

attractions = [
    {"name": "Wicket's Wild Treehouse Drop", "zone": "Forest of Endor", "type": "ride", "thrill": 3, "wait": 10},
    {"name": "Canopy Rope Bridge Walk", "zone": "Forest of Endor", "type": "experience", "thrill": 1, "wait": 5},
    {"name": "Gorax Cave Expedition", "zone": "Forest of Endor", "type": "ride", "thrill": 3, "wait": 25},
    {"name": "Log Drum Spinner", "zone": "Ewok Village", "type": "ride", "thrill": 2, "wait": 15},
    {"name": "Chief Chirpa's Storytelling", "zone": "Ewok Village", "type": "show", "thrill": 1, "wait": 5},
    {"name": "Ewok Cooking Class", "zone": "Ewok Village", "type": "experience", "thrill": 1, "wait": 10},
    {"name": "AT-ST Rampage Coaster", "zone": "Imperial Ruins", "type": "ride", "thrill": 4, "wait": 45},
    {"name": "Bunker Escape Room", "zone": "Imperial Ruins", "type": "experience", "thrill": 2, "wait": 20},
    {"name": "Speeder Bike Chase", "zone": "Speeder Bike Canyon", "type": "ride", "thrill": 4, "wait": 60},
    {"name": "Scout Trooper Training", "zone": "Speeder Bike Canyon", "type": "experience", "thrill": 3, "wait": 15},
    {"name": "Yub Nub Celebration Show", "zone": "Bright Tree Grove", "type": "show", "thrill": 1, "wait": 5},
    {"name": "Endor Cantina", "zone": "Bright Tree Grove", "type": "dining", "thrill": 1, "wait": 10},
]

for a in attractions:
    z = ThemeZone.objects.get(name=a['zone'])
    Attraction.objects.get_or_create(
        name=a['name'],
        defaults={
            'zone': z,
            'attraction_type': a['type'],
            'thrill_level': a['thrill'],
            'current_wait_minutes': a['wait']
        }
    )

guests = [
    {"first": "Luke", "last": "Skywalker", "email": "luke@rebellion.org", "tier": "gold", "height": 172},
    {"first": "Leia", "last": "Organa", "email": "leia@rebellion.org", "tier": "platinum", "height": 150},
    {"first": "Han", "last": "Solo", "email": "han@falcon.com", "tier": "silver", "height": 180},
    {"first": "Wicket", "last": "Warrick", "email": "wicket@endor.net", "tier": "platinum", "height": 80},
    {"first": "Chewie", "last": "Wookiee", "email": "chewie@kashyyyk.com", "tier": "standard", "height": 228},
]

for g in guests:
    Guest.objects.get_or_create(
        email=g['email'],
        defaults={
            'first_name': g['first'],
            'last_name': g['last'],
            'membership_tier': g['tier'],
            'height_cm': g['height']
        }
    )

time_slots_data = [
    (time(9,0), time(9,30)),
    (time(10,0), time(10,30)),
    (time(11,0), time(11,30)),
    (time(13,0), time(13,30)),
    (time(14,0), time(14,30)),
    (time(15,0), time(15,30)),
]

for ride_name in ["Speeder Bike Chase", "AT-ST Rampage Coaster", "Wicket's Wild Treehouse Drop"]:
    ride = Attraction.objects.get(name=ride_name)
    for start, end in time_slots_data:
        TimeSlot.objects.get_or_create(
            attraction=ride,
            start_time=start,
            defaults={'end_time': end, 'max_fastpasses': 25}
        )

print("Setup Complete")
