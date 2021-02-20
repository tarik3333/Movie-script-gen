from selenium import webdriver
import time
import pickle
from movielist import liste
import requests

#print(liste)
driver = webdriver.Chrome()

for i in range(len(liste)):
    path = "https://imsdb.com/scripts/{}.html".format(liste[i])
    req = requests.get(path)
    if req.status_code == requests.codes['ok']:
        print(liste[i])
        driver.get(path)
        path1 = "/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre"
        dos = open("scripts.txt","a")
        time.sleep(1)
        try:
            dos.write(driver.find_element_by_xpath(path1).text)
            print(liste[i],"completed")
        except UnicodeEncodeError:
            pass


