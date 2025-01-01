from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverSingleton:
    _driver = None

    @staticmethod
    def get_driver():
        if DriverSingleton._driver is None:
            DriverSingleton._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return DriverSingleton._driver