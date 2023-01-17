'''
Will automate targeting webpage using Selenium WebDriver
 By.XPATH
 By.ID
 By.CLASS-NAME
 By.TAG_NAME
 By.NAME
 By.CSS_SELECTOR

'''

import time
from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



with open("logs/auto_sel_kb_searchbox_selenium.log", 'a') as log_file:

    log_file.write(f'starting: {datetime.now()} \n')
    log_file.write("tester: Daniel Yoo \n")

    log_file.write('Creating Chrome browser... \n')
    browser_chrome = webdriver.Chrome()
    log_file.write('Created Chrome browser... \n')
    #browser_edge = webdriver.Edge()

    log_file.write('Loading: https://www.selenium.dev/... \n')
    browser_chrome.get('https://www.selenium.dev')
    log_file.write('Loaded: https://www.selenium.dev/... \n')
    #browser_edge.get('https://www.selenium.dev')
    log_file.write('Maximizing: Chrome Browser... \n')
    browser_chrome.maximize_window()
    log_file.write('Maximized: Chrome Browser... \n')
    #browser_edge.maximize_window()

    #WebElement

    #target_searchbox_chrome = browser_chrome.find_element(By.CLASS_NAME, "DocSearch-Search-Icon")
    #target_searchbox_chrome.send_keys('CCTB reviews')
    #target_searchbox_chrome.submit()
    #target_searchbox_chrome.click()

    #ActionChains(browser_chrome).key_up(Keys.CONTROL).send_keys('k').perform()
    log_file.write('Creating: ActionChains(browser_chrome) \n')
    ActionChains(browser_chrome).key_down(Keys.CONTROL).send_keys('k').perform()
    log_file.write('Created: ActionChains(browser_chrome) \n')

    log_file.write('Waiting: Elements to load... \n')
    time.sleep(1)
    #wait = WebDriverWait(browser_chrome, 5)
    #element = wait.until(EC.visibility_of_element_located(
    # (By.XPATH, '/html/body/div[2]/div/header')))
    log_file.write('Sending Keys: "actions"... \n')
    ActionChains(browser_chrome).key_up(Keys.CONTROL).send_keys("actions").perform()
    log_file.write('Sent Keys: "actions"... \n')




    #ActionChains(browser_edge).key_down(Keys.CONTROL).send_keys('k').perform()
    #ActionChains(browser_edge).key_up(Keys.CONTROL).perform()
    #ActionChains(browser_edge).send_keys('actions').perform()



    #target_searchbox_edge = browser_edge.find_element(By.CLASS_NAME, "DocSearch-Search-Icon")
    #target_searchbox_edge.send_keys('CCTB reviews')
    #target_searchbox_edge.submit()
    #target_searchbox_edge.click()
    log_file.write('Waiting: Page to Load... \n')
    time.sleep(5)
    log_file.write('Shutting Down: browser_chrome... \n')
    browser_chrome.quit()
    log_file.write('Shutdown Done: browser_chrome... \n')
    #browser_edge.quit()
