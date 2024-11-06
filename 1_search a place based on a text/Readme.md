To create a Python script that uses the Google Places API to search for a place based on a text query, you will need to follow these steps:

### Step 1: Set Up Your Google Cloud Project
1. Go to the Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Create a new project.
3. Enable the **Places API** for your project.
4. Set up billing (if not already done) and create an API key for accessing the Google Places API.

### Step 2: Install Required Libraries
You need to install the `requests` library to make HTTP requests to the Google Places API. You can install it using pip:

```bash
pip install requests
```

### Step 3: Python Code to Search a Place

Here is an example Python script that uses the Google Places API to search for a place based on a text query:

```python
import requests

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
        results = response.json().get('results', [])
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
```

### Step 4: Explanation of Parameters
- **`query`**: The text string for the search, e.g., "restaurants in New York" or "coffee near me".
- **`api_key`**: Your Google Places API key.
- **`location`** (optional): A latitude/longitude pair (e.g., "40.7128,-74.0060") for more localized search.
- **`radius`** (optional): The radius in meters within which to search around the `location`. For example, a radius of 5000 meters (5 km).

### Step 5: Handling the Response
The Google Places API will return a JSON response with a list of places that match the query. The `results` key contains a list of places, each with information like:
- `name`: The name of the place.
- `formatted_address`: The address of the place.
- `rating`: The average user rating of the place (if available).
- `place_id`: A unique identifier for the place, which can be used to get more details via the Google Places API.

### Example Output

```plaintext
Name: Joe's Pizza
Address: 7 Carmine St, New York, NY 10014, USA
Rating: 4.5
Place ID: ChIJa0mxWQ8rYIkRnzfz2cy_t6M
--------------------------------------------------
Name: John's Pizzeria
Address: 278 Bleecker St, New York, NY 10014, USA
Rating: 4.3
Place ID: ChIJk_aQ3Q8rYIkR9rszj0uQU8s
--------------------------------------------------
```

### Step 6: Make It Dynamic
You can modify this script to take user input for the search query or location. For example:

```python
if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_API_KEY"
    query = input("Enter the place or type of business you want to search: ")
    location = input("Enter location (latitude,longitude) [optional]: ")
    radius = input("Enter radius in meters [optional]: ")
    
    search_place(api_key, query, location, radius)
```

This way, users can interactively enter the search parameters.

---

Make sure you secure your API key by restricting its usage in the Google Cloud Console, so it can only be used by your application.