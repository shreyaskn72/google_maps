import requests
import json


def search_place(api_key, query, location=None, radius=None):
    # Base URL for Google Places Text Search API
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Prepare parameters for the API request
    params = {
        'query': query,
        'key': api_key
    }

    # Optional parameters
    if location:
        params['location'] = location
    if radius:
        params['radius'] = radius

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        response_json = response.json()
        response_dict = json.dumps(response_json, indent=4)
        print("response dict is")
        print(response_dict)
        results = response_json.get('results', [])
        if results:
            for place in results:
                print(f"Name: {place['name']}")
                print(f"Address: {place['formatted_address']}")
                print(f"Rating: {place.get('rating', 'No rating available')}")
                print(f"Place ID: {place['place_id']}")
                print('-' * 50)
        else:
            print("No places found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    # Replace with your own API key
    api_key = "YOUR_GOOGLE_API_KEY"

    # Query to search for a place
    query = "restaurants in New York"

    # Optionally, you can specify location (latitude, longitude) and radius (in meters)
    location = "40.7128,-74.0060"  # New York City coordinates
    radius = 5000  # Search within a 5km radius

    # Search for the place
    search_place(api_key, query, location, radius)