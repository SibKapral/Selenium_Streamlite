import streamlit as st
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

URL = "https://www.google.ru/"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20


@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get(URL)
data = driver.page_source

soup = BeautifulSoup(data, features="lxml")

frame_info = soup.find_all(class_='pHiOh')


st.write(frame_info)