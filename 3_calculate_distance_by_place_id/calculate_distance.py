import requests

# Your Google API key
API_KEY = 'YOUR_GOOGLE_API_KEY'

# Base URLs for Google Places API and Google Distance Matrix API
PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'
DISTANCE_MATRIX_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'


# Function to get place details (latitude and longitude) from place_id
def get_place_coordinates(place_id):
    params = {
        'place_id': place_id,
        'key': API_KEY
    }
    response = requests.get(PLACE_DETAILS_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'OK':
            # Extract latitude and longitude from geometry
            location = data['result'].get('geometry', {}).get('location', {})
            lat = location.get('lat')
            lng = location.get('lng')
            if lat is not None and lng is not None:
                return lat, lng
            else:
                print("Coordinates not found for the place.")
        else:
            print(f"Error fetching place details: {data.get('status')}")
    else:
        print(f"Failed to fetch place details. HTTP Status code: {response.status_code}")

    return None, None


# Function to calculate distance between two places using Google Distance Matrix API
def get_distance_between_places(place_id_1, place_id_2):
    # Get coordinates for both places
    lat1, lng1 = get_place_coordinates(place_id_1)
    lat2, lng2 = get_place_coordinates(place_id_2)

    if lat1 is None or lat2 is None:
        return "Could not get coordinates for one or both places."

    # Construct the parameters for the Distance Matrix API
    origins = f"{lat1},{lng1}"
    destinations = f"{lat2},{lng2}"

    params = {
        'origins': origins,
        'destinations': destinations,
        'key': API_KEY
    }

    # Request distance matrix data
    response = requests.get(DISTANCE_MATRIX_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get('status') == 'OK':
            # Extract the distance and duration
            elements = data.get('rows', [])[0].get('elements', [])[0]
            distance = elements.get('distance', {}).get('text', 'N/A')
            duration = elements.get('duration', {}).get('text', 'N/A')

            return f"Distance: {distance}, Duration: {duration}"
        else:
            print(f"Error fetching distance: {data.get('status')}")
    else:
        print(f"Failed to fetch distance data. HTTP Status code: {response.status_code}")

    return "Error calculating distance."


# Example usage
place_id_1 = 'ChIJu3uL1VKe5kcRw62oRyx7rw0'  # Replace with the place_id of the first place
place_id_2 = 'ChIJu3uL1VKe5kcRw62oRyx7rw1'  # Replace with the place_id of the second place

distance_info = get_distance_between_places(place_id_1, place_id_2)
print(distance_info)