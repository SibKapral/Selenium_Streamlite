import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Get the path to chromedriver in the current directory
def selen_func(log, pas):
    chrome_driver_path = "./chromedriver"

    #@st.cache_resource
    def get_driver():
        return webdriver.Chrome(ChromeDriverManager().install())(options=options)



    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = get_driver()
    
    #try:
    #    driver.quit()
    #except:
    #    st.write("good quit")

    try:
        driver.get("https://hh.ru/account/login?customDomain=1")
        sleep(5)
        print(1)
        st.write("Scraper activation (preparation for scraping 1/5)")
    except:
        st.write("1/5-non")
    try:
        pass_button = driver.find_elements(By.CLASS_NAME, 'bloko-link.bloko-link_pseudo')
        pass_button[1].click()
        sleep(5)
        print(2)
        st.write("Site's home page (preparation for scraping 2/5)")
    except:
        st.write("2-non")
    try:
        search = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')
        print(len(search))
        sleep(5)
        print(3)
        st.write("Initialization page (preparation for scraping 3/5)")
    except:
        st.write("3-non")
    try:
        search[1].send_keys(f'{log}')
        search[2].send_keys(f'{pas}')
        sleep(5)
        print(4)
        st.write("Login and password input (preparation for scraping 4/5)")
    except:
        st.write("4-non")
    try:
        search[2].send_keys(Keys.ENTER)
        sleep(5)
        print(5)
        st.write("Completion of initialization (preparation for scraping 5/5)")
    except:
        st.write("5-non")
    return driver
#for percent_complete in range(100):
#    driver.get('https://hh.ru/applicant/vacancy_response?vacancyId=85931286')
