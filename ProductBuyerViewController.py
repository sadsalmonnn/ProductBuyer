from ProductBuyerModel import ProductBuyerModel, websites
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import Dict

class ProductBuyerViewController:
    _model: ProductBuyerModel
    _userweb: str

    def __init__(self, model:ProductBuyerModel):
        self.model = model

    @staticmethod
    def websiteValidtity(URL):
        #TODO: Implement
        if URL == "":
            return False
        return True

    def run(self):

        while True:
            website = ""

            while not ProductBuyerViewController.websiteValidtity(website):
                print("Please enter the URL of the website to use TCG Scraper:")
                website = input()
            
            print("What product are you searching for?")
            product = input().lower() # Program assumes the product entered is exact and correct

            products = self.model.getProducts(website, product)

            if self.displayProducts(products):
                break

        #TODO: Select product to return avail
        #TODO: Set amount of time
        #TODO: Notify
        #TODO: BUY
            
    def displayProducts(products : Dict[str, bool]) -> bool:
        if len(products == 0):
            print("No Products available")
            return False
        
        print("Here's the list of related products:")
        for x in products:

            availability = "Out of Stock"

            if products[x]:
                availability = "In Stock"
            print("\n" + str(x) + "." , products[x] , "->" , availability)

        return True


    def buy(self):
        # Notify user playing noise repeatedly
        # Once user responds, buy
        print("Succesfully bought.")
        pass

    def update(self):
        pass