import time
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

print("Creating: Web driver Chrome...")
driver = webdriver.Chrome()
print("Created: Web driver Chrome...")

print("Opening: https://www.canadianctb.ca/...")
driver.get("https://www.canadianctb.ca/")
print("Opened: https://www.canadianctb.ca/...")

print("Maximizing: Browser...")
driver.maximize_window()
print("Maximized: Browser...")

print("Waiting: Elements to Load...")
time.sleep(1)

print("Targeting: Student Lounge Menu...")
click_lounge = driver.find_element(
    By.XPATH, " /html/body/nav[2]/div[2]/div/ul[1]/li[2]/a ")

print("Clicking: Virtual Student Lounge Menu...")
click_lounge.click()

print("Waiting: Page to Load...")
time.sleep(3)

print("Closing: Chrome Browser...")
driver.close()

print("Quitting: Web driver Chrome...")
driver.quit()
