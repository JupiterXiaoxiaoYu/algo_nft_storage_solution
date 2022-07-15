from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import os

# 指定浏览器为chrome，需先把selenium的chromeDriver放在python安装目录
option = ChromeOptions()


option.add_argument(f"--user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Google\\Chrome\\User Data")
option.add_argument(" --profile-directory=Profile 1")
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver=webdriver.Chrome(r'C:/Users/Jupiter/Desktop/chromedriver.exe',chrome_options=option)
driver.get(r'https://app.storage.chainsafe.io/cids')
time.sleep(10)

# 窗口最大化，示例网页上半部分有个大图（拿手机的人手），加载完毕会耗费几秒钟，请耐心等待
driver.maximize_window()
time.sleep(10)

data = pd.read_csv('C:/Users/Jupiter/Desktop/v1metadata.csv')
dict_data = dict(zip(data['ipfs_url'].str[7:],data['asset_name']))
filename = "C:/Users/Jupiter/Desktop/pin_number.txt"
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

    # 输入英文公司名
    driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[1]/label[1]/div/input').send_keys(asset_name)


    driver.find_element("xpath",'//*[@id="root"]/div/article/section/article/section/section/div/div[1]/label[2]/div/input').send_keys(cid)
    # 输入完毕，点击确认按钮。。。因为是测试用，这里就不真的点击了，注释掉下方代码
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
