import json
import requests

url = 'https://api.estuary.tech/pinning/pins'

body=json.dumps({
    'name': '', #replace with the file name 
    'cid': '', #replace with the cid that you want to pin
})
headers = {
  'Authorization':'Bearer REPLACE_WITH_YOUR_API_KEY',
  
}

response = requests.request("POST", url, headers=headers, data=body)

print(response.text)