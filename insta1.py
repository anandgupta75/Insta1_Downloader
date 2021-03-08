import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import uuid
import sys
header={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
#driver_path="C:\Users\Arun\Downloads\Compressed\chromedriver_win32\chromedriver"
r1=requests.get("https://www.instagram.com/p/CLJxKzbF7Ji/",headers=header)
#print(r1.text)
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver1=webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
SCROLL_PAUSE_TIME = 5

#driver1.get('https://www.instagram.com/emilia_clarke/')
driver1.get('https://www.instagram.com/accounts/login/')
last_height=driver1.execute_script("return document.documentElement.scrollHeight")
time.sleep(5)
driver2=driver1.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
driver2.send_keys(sys.argv[1])
time.sleep(2)
driver3=driver1.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
time.sleep(2)
driver3.send_keys(sys.argv[2])
driver4=driver1.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]').click()
time.sleep(6)
driver1.get(sys.argv[3])
links=[]
links2=[]
while True:

    time.sleep(SCROLL_PAUSE_TIME)
    driver1.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(SCROLL_PAUSE_TIME)
    s1 = BeautifulSoup(driver1.page_source, "html.parser")
    for i in s1.find_all('a',href=True):
        if i['href'].startswith('/p'):
            links.append('https://instagram.com'+i['href'])
            #print('https://instagram.com'+i['href'])

    new_height = driver1.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    for i3 in links:
        if i3 not in links2:
            links2.append(i3)
        else:
            pass
    print(len(links2))

with open('link5.txt','w')as s2:
    for line in links2:
        s2.writelines(line+"\n")

with open('link5.txt', 'r') as s:
    for line in s:
        driver1.get(line)
        time.sleep(5)
        s4 = BeautifulSoup(driver1.page_source, "html.parser")
        if s4.find("div", {"class": "eLAPa kPFhm"}) is None:
            continue
        s2 = s4.find_all('div', class_= ['eLAPa kPFhm','_97aPb wKWK0'])[0].find_all('img')[0].get('src')
        with open(str(uuid.uuid4()) + ".jpg", "wb")as s11:
            s10 = requests.get(s2)
            s11.write(s10.content)
    driver1.close()
