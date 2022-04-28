import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date

class UPNOUT():

    def __init__(self,driver):
        self.driver = driver
        self.maturity_path = "//input[@name='periodInput']"
        self.currency_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[1]/div[3]/select"
        self.amount_path =  "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-input-holder[1]/div[3]/div[1]/input[1]"
        self.underlyng_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/search-select-list[1]/div[3]/input[1]"
        self.solvefor_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[2]/div[3]/select"
        self.participaion_path = "(//input[@type='text'])[10]"
        self.barrier_path = "(//input[@type='text'])[11]"
        self.premium_path = "(//input[@type='text'])[13]"

    def Maturity(self,maturity):
        self.driver.find_element_by_xpath(self.maturity_path).clear()
        self.driver.find_element_by_xpath(self.maturity_path).send_keys(maturity)

    def Currency(self,currency):
        self.driver.find_element_by_xpath(self.currency_path).send_keys(currency)

    def Amount(self,amount):
        self.driver.find_element_by_xpath(self.amount_path).clear()
        self.driver.find_element_by_xpath(self.amount_path).send_keys(amount)

    def Solvefor(self,solvefor):
        self.driver.find_element_by_xpath(self.solvefor_path).send_keys(solvefor)

    def Underlyng(self,underlyng):
        self.driver.find_element_by_xpath(self.underlyng_path).send_keys(underlyng)

    def Participation(self, participation):
        self.driver.find_element_by_xpath(self.participaion_path).clear()
        self.driver.find_element_by_xpath(self.participaion_path).send_keys(participation)

    def Barrier(self, barrier):
        self.driver.find_element_by_xpath(self.barrier_path).clear()
        self.driver.find_element_by_xpath(self.barrier_path).send_keys(barrier)

    def Premium(self, premium):
        self.driver.find_element_by_xpath(self.premium_path).clear()
        self.driver.find_element_by_xpath(self.premium_path).send_keys(premium)