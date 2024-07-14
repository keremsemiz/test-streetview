import random
import requests
import os

API_KEY = 'APIKEYOTHERFILEIMNOTLEAKINGITHAHAHA'

known_locations = [
    (40.748817, -73.985428),  # New York, USA
    (48.858844, 2.294351),    # Paris, France
    (35.689487, 139.691711),  # Tokyo, Japan
    (51.507351, -0.127758),   # London, UK
    (34.052235, -118.243683), # Los Angeles, USA
    (55.755825, 37.617298),   # Moscow, Russia
    (40.416775, -3.703790),   # Madrid, Spain
    (52.520008, 13.404954),   # Berlin, Germany
    (37.774929, -122.419418), # San Francisco, USA
    (39.904202, 116.407394),  # Beijing, China
]

def get_random_known_location():
    return random.choice(known_locations)

def get_street_view_image(latitude, longitude, heading, filename):
    image_url = (
        f"https://maps.googleapis.com/maps/api/streetview?"
        f"size=1280x720&location={latitude},{longitude}&"
        f"fov=90&heading={heading}&pitch=0&key={API_KEY}"
    )
    response = requests.get(image_url)
    if response.status_code == 200 and response.headers['Content-Type'].startswith('image'):
        with open(filename, "wb") as file:
            file.write(response.content)
        return True
    else:
        return False

if __name__ == "__main__":
    lat, lon = get_random_known_location()
    print(f"Fetching Street View images for coordinates: {lat}, {lon}")
    
    headings = [0, 45, 90, 135, 180, 225, 270, 315]
    for heading in headings:
        filename = f"street_view_{heading}.png"
        if get_street_view_image(lat, lon, heading, filename):
            print(f"Saved {filename}")
        else:
            print(f"Failed to fetch image for heading {heading}")