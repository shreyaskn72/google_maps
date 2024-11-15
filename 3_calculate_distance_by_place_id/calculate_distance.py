import requests

# Your Google API key
API_KEY = 'YOUR_GOOGLE_API_KEY'  # Replace with your actual API key

# Base URL for Google Distance Matrix API
DISTANCE_MATRIX_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'


# Function to calculate distance between two places using their place_ids
def get_distance_between_places(place_id_1, place_id_2):
    # Construct the parameters for the Distance Matrix API using place_ids directly
    params = {
        'origins': f'place_id:{place_id_1}',
        'destinations': f'place_id:{place_id_2}',
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