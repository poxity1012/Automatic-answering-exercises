
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import parsel



driver = webdriver.Chrome()
driver.get('https://www.jsyks.com/kmy-mnks')


lis = driver.find_elements(By.CSS_SELECTOR,'.Content li')
for li in lis:
    num = li.get_attribute('c')
    link = f'https://tiba.jsyks.com/Post/{num}.htm'
    html_data = requests.get(url=link).text

    selecter = parsel.Selector(html_data)
    answer = selecter.css('#question h1 u::text').get()

    if answer == '对':
        answer = '正确'
    elif answer == '错':
        answer == '错误'


    bs = li.find_elements(By.CSS_SELECTOR,'b')
    for b in bs:
        choose = b.text
        if answer in choose:
            b.click()







input("Press Enter to close the browser...")
driver.quit()
