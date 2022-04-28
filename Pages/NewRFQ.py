
class Create_RFQ:

    def __init__(self,driver):
        self.driver = driver
        self.send_rfq_path = "//button[contains(text(),'Send RFQ')]"
        self.reload_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-product[1]/windows-manager[1]/as-split[1]/as-split-area[4]/wm-window[1]/app-rfq[1]/div[1]/div[1]/div[2]/div[1]/custom-status-layer[1]/div[1]"

    def Send_rfq(self):
        self.driver.find_element_by_xpath(self.send_rfq_path).click()

    def Reload_rfq(self):
        self.driver.find_element_by_xpath(self.reload_path).click()

