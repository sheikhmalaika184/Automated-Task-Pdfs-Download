from tkinter import *
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


Keyword = "HERTZ"

#change this driver path
DRIVER_PATH = '/Users/malaikasheikh/python/chromedriver'
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

def make_request(name):
    try:
        url = "https://lowtaxinfo.com/allencounty"
        driver.get(url)
        time.sleep(7)
        form_tag = driver.find_element(By.TAG_NAME,"form")
        input_tags = form_tag.find_elements(By.TAG_NAME,"input")
        button = form_tag.find_element(By.TAG_NAME,"button")
        for input_tag in input_tags:
            if(input_tag.get_attribute("id") == "owner-name"):
                input_tag.send_keys(name)
                break
        button.click()
        time.sleep(5)
        table_tag = driver.find_element(By.TAG_NAME,"table")
        tr_tags = table_tag.find_elements(By.TAG_NAME,"tr")
        pdfs_links = []
        for tr in tr_tags:
            a_tags = tr.find_elements(By.TAG_NAME,"a")
            for a_tag in a_tags:
                if(a_tag.get_attribute("title") == "Tax Bill"):
                    pdfs_links.append(a_tag.get_attribute("href"))
                    break
        i = 0
        for pdf_link in pdfs_links:
            driver.get(pdf_link)
            time.sleep(10)
            pdf_url = driver.current_url
            urllib.request.urlretrieve(pdf_url, f"taxbill{i}.pdf")
            i = i + 1
    except Exception as e:
        print(e)

make_request(Keyword)