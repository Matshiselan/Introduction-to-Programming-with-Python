from geopy.geocoders import Nominatim

def main():
    location_name = input("Enter a location name: ")
    coordinates = get_location_coordinates(location_name)
    if coordinates:
        print(coordinates[0], coordinates[1])
    else:
        print(f"Location '{location_name}' not found.")

def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="location_finder")
    location = geolocator.geocode(location_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
    
if __name__ == "__main__":
    main()

   