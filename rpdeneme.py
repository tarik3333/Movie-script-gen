from selenium import webdriver
import time
import pickle
from movielist import liste
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/alicheraghpour/Desktop/scriptwriting/chromedriver')

for i in range(len(liste)):
    path = "http://shakespeare.mit.edu/Poetry/sonnet.{}.html".format(liste[i])
    # print(path)
    req = requests.get(path)
    if req.status_code == requests.codes['ok']:
        print(liste[i])
        driver.get(path)
        path1 = "/html/body/blockquote"
        dos = open("scripts.txt","a")
        time.sleep(1)
        try:
            dos.write(driver.find_element(By.XPATH, path1).text)
            print(liste[i],"completed")
        except UnicodeEncodeError:
            pass


