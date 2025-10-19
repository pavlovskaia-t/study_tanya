import os
import requests
from urllib.parse import quote, urlparse

BASE = "http://127.0.0.1:8080"
IMG_PATH = "kort.jpg"

# 1) UPLOAD
with open(IMG_PATH, "rb") as f:
    r = requests.post(f"{BASE}/upload", files={"image": f})
r.raise_for_status()
image_url = r.json()["image_url"]
print("Uploaded:", image_url)

# 2) GET (вернуть ссылку в JSON)
filename = os.path.basename(urlparse(image_url).path)
encoded = quote(filename)

r = requests.get(f"{BASE}/image/{encoded}", headers={"Content-Type": "text"})
r.raise_for_status()
print("GET (text):", r.json())

# 3) DELETE
r = requests.delete(f"{BASE}/delete/{encoded}")
r.raise_for_status()
print("DELETE:", r.json())
