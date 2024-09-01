from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

query = input('what do you want to search today: ')
url = 'https://wisemarket.com.pk/?srsltid=AfmBOorBaXIVlsSm_vJjX7tP6siTrmMX3Enw9kK5OVc7vz-QnYCLDTMi'
driver = webdriver.Chrome()
driver.get(url)

search_box = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/div/div[3]/label/input')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

names = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[3]')
ratings = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[4]/div[1]/span')
shipping_status = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[4]/div[1]/div[2]')
prices = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[4]/a/div/span')
status = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[4]/div[2]')