import json
import requests

url = 'https://api.estuary.tech/pinning/pins'

body=json.dumps({
    'name': 'Wushu Chi #0421',
    'cid': 'bafybeifxw3cxljzphehftxlhriqzl6m3qkjq6ntsa5jgcwlyrftaocec7q',
})
headers = {
  'Authorization':'Bearer ESTb382bc05-0673-4fe7-92c7-79332e557f4aARY',
  
}

response = requests.request("POST", url, headers=headers, data=body)

print(response.text)