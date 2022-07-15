# Introduction
These scripts provides various way for you to repin your cid.

# Step 1 - Find a IPFS service provider
You need to find a service provider to pin your cid, some of them require you to apply for a API key for pinning.

My recommendation is:

chainsafe: https://app.storage.chainsafe.io/cids (No API key required)

estuary: https://estuary.tech/home (Need to apply for access)

web3.storage: https://web3.storage/tokens/ (Need to apply for API key)

nft.storage: https://nft.storage/manage/ (Need to apply for API key)

Approval for API access application are usually very fast by those providers.

# Step 2 - Repin your cid
## Optiona A
For chainsafe, you need to install some python dependencies as well as chromedriver to run the automatic form filling script (pin.py), to batch pin cids.

No api key is required. However, this requires you to replace some file paths that matches your own.

## Option B
For other three providers, you need to first apply for an API key, and then use this API key to send HTTP request to repin your cid, according to the docs provided by the specfic service provider you choose.

You need to change the pin_api.py file to match the form of sending HTTP request accordingly and you may also need to use pandas to read your obtained ipfs_data file.

If you need help, please contact: jupiterxiaoxiaoyu@gmail.com
