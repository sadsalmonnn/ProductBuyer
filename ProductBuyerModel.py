from WebsiteStrategy import WebsiteStrategy
from FactoryWebsiteStrat import FactoryWebsiteStrat
from typing import Dict, List
from DriverSingleton import DriverSingleton

websites = ["Walmart", "Pokedeckstcg"]

class ProductBuyerModel:
    _strategy: WebsiteStrategy
    _stocks: Dict[str, List[str]]
    # {Pokdeckstcg : ["C$289.99", "In Stock"], Walmart : ["C$2.00", "Out of Stock"]}

    def __init__(self):
        self._stocks = {}
        self._strategy = None
        self._webdriver = DriverSingleton.get_driver()
        

    def scrape(self, userweb:str, userprod:str) -> bool:
        self._strategy = FactoryWebsiteStrat.create(userweb)
        prodinfo = self._strategy.scrape(userprod, self._webdriver)

        if len(prodinfo) > 0:
            self._stocks.update({userweb: prodinfo})
        else:
            return False

        return prodinfo[1] == "In Stock"