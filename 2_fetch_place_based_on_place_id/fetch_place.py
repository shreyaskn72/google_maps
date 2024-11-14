import requests
import json

# Your Google Places API key
API_KEY = 'YOUR_GOOGLE_API_KEY'

# Base URL for the Google Places API Place Details endpoint
PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'


# Function to get place details by place_id
def get_place_details(place_id):
    # Construct the request URL with the place_id and API key
    params = {
        'place_id': place_id,
        'key': API_KEY
    }

    # Send the GET request to the Google Places API
    response = requests.get(PLACE_DETAILS_URL, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()

        # Check if the results are found
        if data.get('status') == 'OK':
            return data['result']  # Returns the place details
        else:
            print("Error:", data.get('status'), data.get('error_message', 'No error message'))
    else:
        print("Failed to fetch data. HTTP Status code:", response.status_code)

    return None


# Function to extract address components
def extract_address_components(address_components):
    street = city = state = zip_code = country = None

    for component in address_components:
        types = component.get('types', [])
        long_name = component.get('long_name', '')

        if 'street_number' in types:
            street = long_name
        elif 'route' in types:
            street = f"{street} {long_name}" if street else long_name
        elif 'locality' in types:
            city = long_name
        elif 'administrative_area_level_1' in types:
            state = long_name
        elif 'postal_code' in types:
            zip_code = long_name
        elif 'country' in types:
            country = long_name

    return street, city, state, zip_code, country


# Example usage
place_id = 'ChIJu3uL1VKe5kcRw62oRyx7rw0'  # Replace with your own place_id
place_details = get_place_details(place_id)

if place_details:
    print("full response")
    print(json.dumps(place_details, indent=4))

    # Extract the formatted address and components
    formatted_address = place_details.get('formatted_address', 'No address available')
    address_components = place_details.get('address_components', [])

    street, city, state, zip_code, country = extract_address_components(address_components)

    print("Formatted Address:", formatted_address)
    print("Street:", street if street else "Not available")
    print("City:", city if city else "Not available")
    print("State:", state if state else "Not available")
    print("Zip Code:", zip_code if zip_code else "Not available")
    print("Country:", country if country else "Not available")