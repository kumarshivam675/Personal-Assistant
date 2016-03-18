import googlemaps
# AIzaSyDZ1j43JoV6TXYJHbarLJHFl73YnQtrWx4    AIzaSyDDWvtSjW9IgdVxzHEf1H5pH20p1rP4lwo
# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='AIzaSyDDWvtSjW9IgdVxzHEf1H5pH20p1rP4lwo')

# Geocoding and address
geocode_result = gmaps.geocode('IIIT-Bangalore')
print geocode_result

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
#directions_result = gmaps.directions("IIIT Bangalore","Majestic", mode="transit", departure_time=now)

