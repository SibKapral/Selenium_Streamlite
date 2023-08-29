import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Get the path to chromedriver in the current directory
chrome_driver_path = "./chromedriver"

@st.cache_resource
def get_driver():
    return webdriver.Chrome(options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()


email = st.text_input('Movie title', 'Email')
password = st.text_input('Movie title', 'Password')

if st.button('Send resume'):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    driver.get("https://hh.ru/account/login?customDomain=1")
    sleep(5)
    print(1)
    pass_button = driver.find_elements(By.CLASS_NAME, 'bloko-link.bloko-link_pseudo')
    pass_button[1].click()
    sleep(5)
    print(2)
    search = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')
    print(len(search))
    sleep(5)
    print(3)
    search[1].send_keys(f'{email}')
    search[2].send_keys(f'{password}')
    sleep(5)
    print(4)
    search[2].send_keys(Keys.ENTER)
    sleep(5)
    print(5)
    for percent_complete in range(100)
        driver.get('https://hh.ru/applicant/vacancy_response?vacancyId=85931286')