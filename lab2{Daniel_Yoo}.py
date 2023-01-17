import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

print("Creating: browser_chrome... ")
browser_chrome = webdriver.Chrome()
print("Created: browser_chrome... ")

print("Opening: https://en.wikipedia.org/... ")
browser_chrome.get("https://en.wikipedia.org/")
print("Opened: https://en.wikipedia.org/... ")

print("Maximizing: Browser... ")
browser_chrome.maximize_window()
print("Maximizing: Browser... ")

print("Waiting: Loading Page... ")
browser_chrome.implicitly_wait(20)

print("Checking: Title and URL... ")
if browser_chrome.title == ("Wikipedia, the free encyclopedia") and browser_chrome.current_url == ("https://en.wikipedia.org/wiki/Main_Page"):
    print(browser_chrome
          .title)
    print(browser_chrome
          .current_url)
else:
    print("Wrong URL and Title...")

print("Waiting: Pages to load...")
time.sleep(2)

print("Targeting: Search Box... ")
search = browser_chrome.find_element(By.ID, "searchInput").click()
print("Targeted: Search Box... ")

print("Waiting: Page to load... ")
time.sleep(1)


print("Sending Keys: Python (programming language) ")
searchInput = browser_chrome.find_element(
    By.ID, "searchInput").send_keys("Python (programming language)")
print("Sent Keys: Python (programming language) ")

print("Waiting: Page to load... ")
time.sleep(1)

print("Clcking Search: Python (programming language)... ")
searchClick = browser_chrome.find_element(By.ID, "searchButton").click()
print("Clcking Search: Python (programming language) ")

print("Waiting: Page to load... ")
time.sleep(5)

print("Closing: Chrome Browser... ")
browser_chrome.close()

print("Quiting: Web driver Chrome... ")
browser_chrome.quit()
