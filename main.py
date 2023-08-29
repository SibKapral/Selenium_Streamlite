import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

URL = "https://www.google.ru/"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20


firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
driver.get(URL)


driver.get(URL)
data = driver.page_source

soup = BeautifulSoup(data, features="lxml")

frame_info = soup.find_all(class_='pHiOh')


st.write(frame_info)