from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.strikingly.com/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/a[1]").click()
time.sleep(2)
user_ele = driver.find_element(By.NAME, 'user[login]').send_keys('tapu.saha98@gmail.com')
time.sleep(2)
pwd_ele = driver.find_element(By.NAME, 'user[password]').send_keys('123456')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/form/div[4]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[2]/div/div/div[2]/div[8]/div/div[1]/div[1]/div[1]/a").click()
time.sleep(2)


