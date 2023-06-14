from selenium import webdriver
from time import sleep
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import pandas  as pd
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


text = []
hrefs = []
def get_detail(res,index):
    temp = {
        "index":res["index"][index],
        "name":res["name"][index],
        "version":res["version"][index],
        "time":res["time"][index],
        "url":res["url"][index],
        "description":res["description"][index]
    }
    return temp
    

def browser_initial():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://github.com/search?l=&o=desc&p=1&q=stars%3A%3E1000+language%3APython&ref=advsearch&s=stars&type=Repositories')
    return browser


def browser_reinitial(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    return browser

def check_star(s):
    pattern = r'^\d+k$'
    return re.match(pattern,s)



def check_element_exists(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

def get_url(browser):
    try:
        res= []
        for page in range(1,2):#101
            # tags 以 , 隔开
            url = "https://github.com/search?l=&o=desc&p="+str(page)+"&q=stars%3A%3E1000+language%3APython&ref=advsearch&s=stars&type=Repositories"
            browser.get(url)
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "repo-list")))
            repo_cells = browser.find_elements(By.XPATH, '//ul[@class="repo-list"]/li')
            for cell in range(len(repo_cells)):
                # print("cell.text:",cell.text)
                # t= cell.text.split('\n')
                # t = [x for x in t if x != "Sponsor"] 
                # print("cell:",t)
                # data = {
                # "name":t[0] ,
                # "url": "https://github.com/"+t[0],
                # "description":t[1],
                # # "star": t[3],
                # # "tags": t[2],
                # # "update_datetime": t[6],
                # }
                # for d in t:
                #     if "Updated" in d:
                #         data ["update_datetime"] = d                
                # if check_star(t[3]) is None:
                #     data['star'] = t[2]
                #     data["tags"] = ""
                # else:
                #     data['star'] = t[3]
                #     data["tags"] = t[2]
                data = {
                "name":repo_cells[cell].find_elements(By.XPATH,'//div[@class="f4 text-normal"]/a[@class="v-align-middle"]')[cell].text ,
                "url": "https://github.com/"+repo_cells[cell].find_elements(By.XPATH,'//div[@class="f4 text-normal"]/a[@class="v-align-middle"]')[cell].text,
                "description":repo_cells[cell].find_elements(By.XPATH,'//div[@class="mt-n1 flex-auto"]/p[@class="mb-1"]')[cell].text,
                "star": repo_cells[cell].find_elements(By.XPATH,'//a[@class="Link--muted"]')[cell].text,
                
                "update_datetime": repo_cells[cell].find_elements(By.XPATH,'//div[@class="d-flex flex-wrap text-small color-fg-muted"]/div[@class="mr-3"]/relative-time[@class="no-wrap"]')[cell].get_attribute('datetime'),
                }
                "tags": repo_cells[cell].find_elements(By.XPATH,'//a[@class="topic-tag topic-tag-link f6 px-2 mx-0"]')[cell].text,
                # print()
                # topic-tag topic-tag-link f6 px-2 mx-0
                # data["url"] = cell.find_element(By.XPATH,'//div[@class="f4 text-normal"]/a[@class="v-align-middle"]').get_attribute('href')
                # data["description"] = cell.find_element(By.XPATH,'//div[@class="mt-n1 flex-auto"]/p[@class="mb-1"]').text
                # data["star"] = cell.find_element(By.XPATH,'//a[@class="Link--muted"]').text
                # data["update_datetime"] = cell.find_element(By.XPATH,'//div[@class="mt-n1 flex-auto"]/p[@class="mb-1"]').text
                # tag_list = cell.find_elements(By.XPATH,'//div[@class="mt-n1 flex-auto"]/p[@class="mb-1"]').text
                # res.append(data)
        pd.DataFrame(res).to_csv('1.csv')
    except NoSuchElementException:
        print(NoSuchElementException) 

# r =[]
browser = browser_initial()
get_url(browser)

# data = {
#     "name": "",
#     "url": "",
#     "description":"",
#     "star": "",
#     "tags": "",
#     "update_datetime": "",
# }
