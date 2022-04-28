import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
class Payoff_autocall():

    def __init__(self,driver):
        self.driver = driver
        self.name_path = "//input[@type='text']"
        self.maturity_path = "//input[@name='periodInput']"
        self.currency_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[1]/div[3]/select"
        self.amount_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-input-holder[1]/div[3]/div[1]/input[1]"
        self.solvefor_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[2]/div[3]/select"
        self.underlyng_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[3]/div[2]/dynamic-block-content[1]/div[1]/search-select-list[1]/div[3]/input[1]"
        self.Autocall_Observation_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[4]/div[2]/dynamic-block-content[1]/div[1]/period-mask[1]/div[3]/input[1]"
        self.Non_Autocall_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[4]/div[2]/dynamic-block-advanced[1]/div[1]/div[1]/custom-input-holder[1]/div[3]/div[1]/input[1]"
        self.Autocall_trigger_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[5]/div[2]/dynamic-block-content[1]/div[1]/input-list[2]/div[3]/div[1]/label[1]/input[1]"
        self.Downside_type_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[6]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[1]/div[3]/select"
        self.put_level_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[6]/div[2]/dynamic-block-content[1]/div[1]/custom-input-holder[1]/div[3]/div[1]/input[1]"
        self.knock_in_barrier_type_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[6]/div[2]/dynamic-block-content[1]/div[1]/custom-combobox[2]/div[3]/select"
        self.knock_in_barrier_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[6]/div[2]/dynamic-block-content[1]/div[1]/custom-input-holder[3]/div[3]/div[1]/input[1]"
        self.coupon_path= "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[5]/div[2]/dynamic-block-content[1]/div[1]/input-list[1]/div[3]/div[1]/label[1]/input[1]"
        self.reoffer_path ="//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[2]/wm-window[1]/product-main[1]/div[2]/form[1]/div[1]/dynamic-details-block[7]/div[2]/dynamic-block-content[1]/div[1]/custom-input-holder[1]/div[3]/div[1]/input[1]"
        self.create_rfq_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/nav[1]/div[1]/div[1]/wm-tab-switch[3]/div[1]/div[1]/div[3]"

    def Name(self,name):
        self.driver.find_element_by_xpath(self.name_path).clear()
        self.driver.find_element_by_xpath(self.name_path).send_keys(name)

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

    def Autocall_Observation(self,autocall_abservation):
        self.driver.find_element_by_xpath(self.Autocall_Observation_path).clear()
        self.driver.find_element_by_xpath(self.Autocall_Observation_path).send_keys(autocall_abservation)

    def Autocall_trigger_path(self,autocall_trigger):
        self.driver.find_element_by_xpath(self.Autocall_trigger_path).clear()
        self.driver.find_element_by_xpath(self.Autocall_trigger_path).send_keys(autocall_trigger)

    def Non_Autocall(self,non_autocll):
        self.driver.find_element_by_xpath("//dynamic-details-block[4]/div[2]/dynamic-block-advanced/collapse-button/div/button/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.Non_Autocall_path).clear()
        self.driver.find_element_by_xpath(self.Non_Autocall_path).send_keys(non_autocll)

    def Downside_type(self,downside_type):
        self.driver.find_element_by_xpath(self.Downside_type_path).send_keys(downside_type)

    def Put_level(self,put_level):
        self.driver.find_element_by_xpath(self.put_level_path).clear()
        self.driver.find_element_by_xpath(self.put_level_path).send_keys(put_level)

    def Knock_in_barrier_type(self,knock_in_barrier_type):
        self.driver.find_element_by_xpath(self.knock_in_barrier_type_path).send_keys(knock_in_barrier_type)

    def Knock_in_barrier(self,knock_in_barrier):
        self.driver.find_element_by_xpath(self.knock_in_barrier_path).clear()
        self.driver.find_element_by_xpath(self.knock_in_barrier_path).send_keys(knock_in_barrier)

    def Coupon(self,coupon):
        self.driver.find_element_by_xpath(self.reoffer_path).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.reoffer_path).send_keys(coupon)

    def Reoffer(self,reoffer):
        self.driver.find_element_by_xpath(self.reoffer_path).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.reoffer_path).send_keys(reoffer)

    def Create_RFQ(self):
        self.driver.find_element_by_xpath(self.create_rfq_path).click()

