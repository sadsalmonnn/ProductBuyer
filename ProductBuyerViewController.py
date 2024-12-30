from ProductBuyerModel import ProductBuyerModel, websites
from time import sleep

class ProductBuyerViewController:
    _model: ProductBuyerModel
    _userweb: str

    def __init__(self, model:ProductBuyerModel):
        self.model = model

    def displaymenu(self):
        print("Please select one of the following websites:")
        for x in range(len(websites)):
            print("\n" + str(x) + ". " + websites[x - 1])
        print("\n" + str(x + 1) + ". All of the above")

    # def displayproducts(self):
    #     products = self.model.getProducts()
    #     print("Heres the list of products:")
    #     for x in range(len(products)):
    #         print("\n" + str(x) + ". " , products[x - 1])

    def run(self):
        print("What product are you searching for.")
        userprod = input()
        self.displaymenu()
        userweb = int(input())
        # self.displayproducts()

        while True:

            if userweb == len(websites):
                for website in websites:
                    prodavail = self.model.scrape(website, userprod)
                    if prodavail:
                        self.buy()
                    else:
                        sleep(10)

            else:
                prodavail = self.model.scrape(website[userweb], userprod)

                if prodavail:
                    self.buy()
                else:
                    sleep(60)


    def buy(self):
        # Notify user playing noise repeatedly
        # Once user responds, buy
        pass

    def update(self):
        pass