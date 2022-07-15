from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import os

option = ChromeOptions()


option.add_argument(f"--user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Google\\Chrome\\User Data")
option.add_argument(" --profile-directory=Profile 1")
driver=webdriver.Chrome(r'C:/Users/Jupiter/Desktop/chromedriver.exe',chrome_options=option) #Replace the first parameter with your downloaded chromedriver

driver.get(r'https://app.storage.chainsafe.io/cids')
time.sleep(10)

driver.maximize_window()
time.sleep(10)

data = pd.read_csv('C:/Users/Jupiter/Desktop/v1metadata.csv') # Replace this with your own metadata
dict_data = dict(zip(data['ipfs_url'].str[7:],data['asset_name']))
filename = "C:/Users/Jupiter/Desktop/pin_number.txt"  #Replace with your own txt for storing the number/order of NFT that have been pinned 
with open(filename, 'r') as file_to_read:
    pin_number = int(file_to_read.readline())
    file_to_read.close()
print(pin_number)
k=0
for cid, asset_name in dict_data.items():
    k+=1
    if k<=pin_number:
        continue
    
    driver.find_element("xpath",'//*[@id="root"]/div/article/section/div/header/div/button').click()


    driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[1]/label[1]/div/input').send_keys(asset_name)


    driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[1]/label[2]/div/input').send_keys(cid)

    try:
        driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[2]/button[2]').click()
    except:
        time.sleep(10)
        driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[2]/button[2]').click()

    time.sleep(5)
    f2 = open(filename,'r+')
    f2.write(str())
    f2.close()
    print(f'{k}NFT has been pinned')
