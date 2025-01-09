# build autonomous program web scraping data

# this actions to import various module for interact with the web, keyboard and mouse control
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

# create an instances chrome webdriver service

prefs = {
    'download.prompt_for_download': False,
    'download.extensions_to_open': 'xml',
    'safebrowsing.enabled': True,
}
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument('--safebrowsing-disable-download-protection')
driver = webdriver.Chrome(options = options)

# navigate to PRTG URL
driver.get('http://192.168.18.47/')
# maximize the size of windows browser to a full screen
driver.maximize_window()
# clicking warning security from web before goes in
driver.find_element(By.ID, "details-button").click() 
driver.find_element(By.ID, "proceed-link").click()
# log in user and password
driver.find_element(By.ID, "loginusername").send_keys('username')#on line send.keys, please input your PRTG username account
driver.find_element(By.ID, "loginpassword").send_keys('password')#on line send.keys, please input your PRTG password account
driver.find_element(By.ID, "submitter1").click()
# drive to log menu
driver.find_element(By.ID, "logmenuitem").click()
# waiting all elements to be present after click log menu for at least 20 sec
driver.implicitly_wait(30)
time.sleep(2)
# Hover over the main element to trigger the submenu
main_element = driver.find_element(By.CLASS_NAME, 'table_itemcount_selector')
hover = ActionChains(driver).move_to_element(main_element)
hover.perform()
# Find and click the specific submenu element
submenu_element = driver.find_element(By.CSS_SELECTOR, '.table_itemcount_selector a[data-reload*="500"]')
submenu_element.click()
# Locate start date and end date log data alarm
datepicker_start = driver.find_element(By.NAME, "datepicker_dstart_picker")
datepicker_start.clear()
datepicker_start.send_keys("2024-12-30 00:00")
datepicker_start.send_keys(Keys.ESCAPE)
time.sleep(2)
datepicker_end = driver.find_element(By.NAME, "datepicker_dend_picker")
datepicker_end.clear()
datepicker_end.send_keys("2025-01-01 00:00")
datepicker_end.send_keys(Keys.ESCAPE)
time.sleep(4)

# condition looping, the program will running until the nextpage button are not clickable anymore

# This is the start of a loop that continues until a specific condition is met. 
#   Inside the loop, a WebDriverWait instance is created with a timeout of 30 seconds. 
#   The script scrolls to the bottom of the page using JavaScript, sleeps for 1 second, 
#   and then finds an image element using its CSS selector. It waits until this element is clickable,
#   and then performs a right-click (context-click) on it using ActionChains.
while True:
    try:
        wait = WebDriverWait(driver,30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        xml = driver.find_element(By.CSS_SELECTOR, ".tablezoomlink:nth-child(4) > img")
        xmlcheck = wait.until(EC.element_to_be_clickable(xml))
        ActionChains(driver).click(xmlcheck).perform()
        time.sleep(2)
       
        driver.execute_script("window.scrollTo(0, 0);")

        # This part finds the "Next" button using its CSS selector, waits until it's clickable, clicks it, sleeps for 3 seconds, 
        #    sets an implicit wait of 30 seconds, and prints the message "log alarm masih tampil".
        button = driver.find_element(By.CSS_SELECTOR, ".tablenavigation:nth-child(3) > .a_right_on")
        buttoncheck = wait.until(EC.element_to_be_clickable(button))
        button.click()
        time.sleep(3)
        driver.implicitly_wait(30)
        print("log alarm masih tampil")

    # If a TimeoutException occurs (likely because there are no more pages to navigate), the script prints the message "log alarm sudah habis" 
    #   and breaks out of the loop.    
    except TimeoutError:
        print("log alarm sudah habis")
        break

#README
# Overall, this script appears to be automating a web-based process involving navigating to a website, logging in, 
#    selecting options, changing date ranges, downloading or processing data from multiple pages, 
#    and continuing until there are no more pages left. It uses a combination of Selenium and pyautogui for web automation and keyboard/mouse control.