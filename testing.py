from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Instead of directly passing the path as a string, use Service
service = Service(ChromeDriverManager().install())

# 
options = Options()
# adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 




# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service, options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

# Once we have initialized the driver and the web browser, we can open a website
driver.get("https://www.pokemoncenter.com/search/pokemon-surging-sparks-booster-box")

import time
time.sleep(100000)
userprod = "Pokémon TCG: Scarlet & Violet-Surging Sparks Booster Display Box (36 Packs)"
# EC.visibility_of_element_located((By.XPATH, f"//*[@text()='{userprod}']"))
# try:
#     element = WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH, f"//*[@text()='{userprod}']")))
#     element.click()
# except:
#     element = None

# if element != None:
#     span_list = element.find_elements(By.TAG_NAME, "span")
#     for x in span_list:
#         print(x.text)

# Other functions
# print(driver.title) # Website title
# driver.close() # Closes current tab
# driver.quit() # Closes entire browser