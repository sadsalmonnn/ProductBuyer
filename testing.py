from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instead of directly passing the path as a string, use Service
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Once we have initialized the driver and the web browser, we can open a website
driver.get("https://www.pokedeckstcg.com/")

userprod = "pokemon-surging-sparks-booster-box"
try:
    element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.XPATH, f"//*[@data-slug='{userprod}']")))
except:
    driver.quit()
    element = None

if element != None:
    span_list = element.find_elements(By.TAG_NAME, "span")
    for x in span_list:
        print(x.text)

# Other functions
# print(driver.title) # Website title
# driver.close() # Closes current tab
# driver.quit() # Closes entire browser