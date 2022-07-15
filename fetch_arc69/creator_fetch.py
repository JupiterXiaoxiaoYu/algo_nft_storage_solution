import base64
from cgi import print_arguments
import os
import json
import csv
import os,sys,inspect
import pandas
from turtle import pd
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from lib.settings import Settings
from lib.file_helper import check_and_create_path


settings = Settings('fetch_arc69')
myindexer = settings.get_indexer()
OUTPUT_PATH = settings.get_output_folder()

def write_meta_data_to_files():
    account = myindexer.lookup_account_asset_by_creator(address=settings.public_key, limit=10)

    if not 'assets' in account:
        print(f"No assets found in account: {settings.public_key} and {'testnet' if settings.full_settings['testnet'] else 'mainnet'}")
        exit()

    next_token = None
    created_assets = []

    try:
        while True:
            payload = myindexer.lookup_account_asset_by_creator(settings.public_key, next_page=next_token,limit=1000)
            created_assets = created_assets + payload.get('assets')

            next_token = payload.get('next-token', None)
            if next_token is None:
                break

            print(".")

    except Exception as e:
        print(e)

    #del created_assets[4:]
    data = []
    for asset in created_assets:
        asset_id = asset['index']
        asset_name = asset['params']['name']
        ipfs_hash = asset['params']['url']
        data.append((asset_id, asset_name, ipfs_hash))

    print(f"Total assets added: {len(data)}")
    try:
        write_csv_file(data)
    except:
        print(data)
        pandas.DataFrame(data).to_csv('ipfs_data.csv')


def write_csv_file(data):
    sortedData = sorted(data)

    converted_data = []
    csv_header = []

    for asset_id, asset_name, ipfs_hash in sortedData:
        new_asset = {}

        if settings.csv['add_asset_id'] and asset_id:
            new_asset['asset_id'] = asset_id

        if settings.csv['add_asset_name'] and asset_name:
            new_asset['asset_name'] = asset_name

        if settings.csv['add_ipfs_url'] and ipfs_hash:
            new_asset['ipfs_url'] = ipfs_hash

        converted_data.append(new_asset)

        for attribute in new_asset:
            if attribute not in csv_header:
                csv_header.append(attribute)

    csv_file_path = f"{OUTPUT_PATH}/metadata.csv"
    check_and_create_path(csv_file_path)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f: 
        wr = csv.DictWriter(f, fieldnames = csv_header) 
        wr.writeheader()
        wr.writerows(converted_data)

    print(f"Script complete - output can be found here: {OUTPUT_PATH}")


write_meta_data_to_files()