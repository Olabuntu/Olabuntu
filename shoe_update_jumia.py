#SCRAPING_SITE_USING_SELENIUM_BEAUTIFULSOUP_PANDAS_PYAUTOGUI_PYPERCLIP
import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import pyperclip
names =[]
prices =[]
links =[]
for i in range(1,4):

    site = (f'https://www.jumia.com.ng/men-sneakers/?page={i}#catalog-listing')
    a = webdriver.Chrome()
    open = a.get(site)
    b = a.find_elements(By.XPATH ,'//*[@id="content"]/div/div/div[2]/div[1]/div[1]/article')
    pyautogui.sleep(4)
    pyautogui.hotkey('ctrl', 'u')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    p = pyperclip.paste()

    soup = BeautifulSoup(p , 'html.parser')
    all = soup.find_all('article', class_="prd _fb col c-prd")
   
    for x in all:
        name = x.find('h3',class_="name").text
        price = x.find('div',class_="prc").text
        link = x.find('a',class_="core").get('href')
        names.append(name)
        prices.append(price)
        links.append(link)
info =  {'PRODUCT NAMES':names, 'PRODUCT PRICE':prices, 'LINKS':links}
new = pd.DataFrame(info)
new.to_csv(f'SHOE_UPDATE.csv', index = False)


    
    
