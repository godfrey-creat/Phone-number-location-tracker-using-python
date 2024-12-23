import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser  # Import the webbrowser module

key = "ef7fde1035894ca98b743a02784cdd69"  # Geocoder API Key needs to paste here "your key"
number = input("please give your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number, "en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

# Generate a map using Folium
my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)
my_map.save("location.html")

# Open the location on Google Maps
google_maps_url = f"https://www.google.com/maps?q={lat},{lng}"
webbrowser.open(google_maps_url)

print("location tracking completed")
print("Thank you")
