from WalmartStrategy import WalmartStrategy
from WebsiteStrategy import WebsiteStrategy
from PokedeckstcgStrategy import PokedeckstcgStrategy

class FactoryWebsiteStrat:

    @staticmethod
    def create(websitename: str) -> WebsiteStrategy:
        strategy = None

        if websitename == "Walmart":
            strategy = WalmartStrategy.getInstance()
        elif websitename == "Pokedeckstcg":
            strategy = PokedeckstcgStrategy()

        return strategy
