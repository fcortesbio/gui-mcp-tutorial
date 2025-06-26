import os
import requests

# Read key from environment variable

BRD_API_KEY = os.getenv("BRD_API_KEY")
if not BRD_API_KEY:
    raise RuntimeError("BRD_API_KEY not found in local environment.")

headers = {
    "Authorization": f"Bearer {BRD_API_KEY}",
    "Content-Type": "application/json"
    }
data = {
    "zone": "unlocker_mcp",
    "url": "https://geo.brdtest.com/welcome.txt?product=unlocker&method=api",
    "format": "raw"
}

response = requests.post(
    "https://api.brightdata.com/request",
    json=data,
    headers=headers
)
print(response.text)
