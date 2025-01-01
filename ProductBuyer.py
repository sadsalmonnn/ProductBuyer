from ProductBuyerViewController import ProductBuyerViewController
from ProductBuyerModel import ProductBuyerModel

def main():
    model = ProductBuyerModel()
    viewcontroller = ProductBuyerViewController(model)
    viewcontroller.run()

main()