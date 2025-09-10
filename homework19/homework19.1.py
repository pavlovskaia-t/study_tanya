import requests
import json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
data = response.json()

photos_list = data['photos']
for photo in photos_list:
    url = photo['img_src']
    resp = requests.get(url)
    with open(f"mars_photo.jpg", "wb") as f:
        f.write(resp.content)