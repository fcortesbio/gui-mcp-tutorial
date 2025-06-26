import requests

headers = {
    "Authorization": "Bearer 1fecd79436b306e400fa6e1b313c2eec9a16445688b00d97e25899fbd157a5ad",
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