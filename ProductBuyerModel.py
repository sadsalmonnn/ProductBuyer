from WebsiteStrategy import WebsiteStrategy
from FactoryWebsiteStrat import FactoryWebsiteStrat
from typing import Dict

websites = ["Walmart", "Pokedeckstcg"]

class ProductBuyerModel:
    _strategy: WebsiteStrategy
    _websites: Dict[str, Dict[str, int]]

    def __init__(self):
        self._websites = {}

    def scrape(userweb:str, userprod:str) -> bool:
        _strategy = FactoryWebsiteStrat.create(userweb)
        websites[userweb] = _strategy.scrape(userprod)

        prodavail = checkProd(userweb)

        # products = {fdjshf: 1, fjdsfs: 2}
        return prodavail
    
    def getProducts(userweb):
        pass