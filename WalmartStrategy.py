from WebsiteStrategy import WebsiteStrategy

_INSTANCE = None

class WalmartStrategy(WebsiteStrategy):

    def __init__(self):
        pass

    @staticmethod
    def getInstance() -> 'WalmartStrategy':

        if _INSTANCE == None:
            _INSTANCE = WalmartStrategy()

        return _INSTANCE
    
    def scrape():
        pass # TO BE IMPLEMENTED
