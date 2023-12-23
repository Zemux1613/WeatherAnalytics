import requests

# Replace 'your_api_url' with the actual API endpoint you want to scrape
base_url = 'https://dwd.api.proxy.bund.dev/v30/'

# Make a GET request to the API
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Now you can work with the data as needed
    print(data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
    print(response.text)
