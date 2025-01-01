from WebsiteStrategy import WebsiteStrategy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from typing import List

class PokedeckstcgStrategy(WebsiteStrategy):
    _websiteurl:str

    def __init__(self):
        self._websiteurl = "https://www.pokedeckstcg.com"
    
    def scrape(self, userprod : str, webdriver) -> List[str]:
        webdriver.get(self._websiteurl)
        # element = self.get_driver.find_element("xpath", f"//*[@data-slug='{userprod}']")
        userprod = userprod.replace('—', '-').replace(' ', '-').replace('(', '').replace(')', '')
        userprod = re.sub("\s|—", "-", userprod)
        userprod = re.sub("[()]", "", userprod)
        userprod = re.sub("--", "-", userprod)
        # while "--" in userprod:
        #     y = 0
        #     for x in range(len(userprod)):
        #         if y == 1 and userprod[x] != "-":
        #             y = 0
        #         if userprod[x] == "-":
        #             y += 1
        #         if y == 2:
        #             break
        #     else:
        #         userprod = userprod[:x] + userprod[x+1:]



                

        try:
            element = WebDriverWait(webdriver, 30).until( EC.presence_of_element_located((By.XPATH, f"//*[@data-slug='{userprod}']")))
            span_list = element.find_elements(By.TAG_NAME, "span")

            if span_list[2].text == "Add to Cart":
                span_list[2] = "In Stock"
            else:
                span_list[2].text = "Out of Stock"
            
            span_list[1] = span_list[1].text
            return span_list[1:]
        except:
            webdriver.quit()
            return []
        


