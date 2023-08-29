#import streamlit as st
#
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#
#@st.experimental_singleton
#def get_driver():
#    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
#options = Options()
#options.add_argument('--disable-gpu')
#options.add_argument('--headless')
#
#driver = get_driver()
#driver.get('http://example.com')
#
#st.code(driver.page_source)

from selenium import webdriver

# Инициализация драйвера
driver = webdriver.Chrome()

# Получение версии ChromeDriver
version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print(f"ChromeDriver version: {version}")

# Закрытие драйвера

driver.quit()