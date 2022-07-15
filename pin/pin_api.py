import json
import requests
import pandas as pd

ipfs_data = pd.read_csv("C:/Users/Jupiter/Desktop/ipfs_solution/output/fetch_arc69/metadata.csv") # replace with your obtained data from step 1 
url = 'https://api.estuary.tech/pinning/pins' # use estuary as the provider, you can replace with your choice

dict_data = dict(zip(ipfs_data['ipfs_url'].str[7:],ipfs_data['asset_name']))

headers = {
    'Authorization':'Bearer RELACE_HERE', #replace with your own API key
}

for cid, asset_name in dict_data.items():
  body=json.dumps({
      'name': asset_name, #replace with the file name 
      'cid': cid, #replace with the cid that you want to pin
  })
  
  response = requests.request("POST", url, headers=headers, data=body)

  print(response.text)