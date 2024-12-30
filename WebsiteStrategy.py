from abc import ABC, abstractmethod

# Abstract class
class WebsiteStrategy(ABC):
    
    @abstractmethod
    def scrape():
        pass

