from typing import Dict, List, WebDriver, Union, WebElement
from DriverSingleton import DriverSingleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

websites = ["Walmart", "Pokedeckstcg"]

class ProductBuyerModel:
    _products: Dict[str, bool]
    _webdriver: WebDriver
    # {Pokemon Surging sparks : False, Surging sparks booster box : True}

    def __init__(self):
        self._products = {}
        self._webdriver = DriverSingleton.get_driver()

    def getProducts(self, url: str, product: str) -> Dict[str, bool]:
        if not self._updateProductDict(url, product):
            return False
        return self._products


    def _updateProductDict(self, url: str, product: str) -> bool:

        # Looks for a search bar
        try:
            search_bar = WebDriverWait(self._webdriver, 30).until( EC.visibility_of_element_located((By.TAG_NAME, "input")))
        except:
            print("There is no searchable element in this website.")
            return False
        
        # Searches for the product
        search_bar.clear()
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)

        try:
            product_text = WebDriverWait(self._webdriver, 30).until( EC.visibility_of_element_located((By.XPATH, f"//*[text()='{product}']")))
        except:
            print("No products are related to your search.")
            return False
        
        # Checks if the following words are shown on screen
        listofvalidavailwords = ["sold out", "in stock", "available"]
        
        if not isinstance(self._wordschecker(listofvalidavailwords), bool):
            product_text.click()

        while True:
            try:
                parent_element = product_text.find_element(By.XPATH, "..")
            except:
                print("Weird... the element has no parent.")
                return False
            
    def _wordschecker(self, words: List[str]) -> Union[WebElement, bool]:
        for x in words:
            try:
                element = WebDriverWait(self._webdriver, 30).until( EC.visibility_of_element_located(( By.XPATH, f"//*[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='{x.lower()}']" )))
                return element
            except:
                continue
        return False


        

    # def scrape(self, userweb:str, userprod:str) -> bool:
    #     self._strategy = FactoryWebsiteStrat.create(userweb)
    #     prodinfo = self._strategy.scrape(userprod, self._webdriver)

    #     if len(prodinfo) > 0:
    #         self._stocks.update({userweb: prodinfo})
    #     else:
    #         return False

    #     return prodinfo[1] == "In Stock"