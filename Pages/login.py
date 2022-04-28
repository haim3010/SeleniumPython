
class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_path = "//input[@type='text']"
        self.password_path = "//input[@type='password']"
        self.login_button_path ="//button[@type='submit']"


    def login(self,username,password):
        self.driver.find_element_by_xpath(self.username_path).send_keys(username)
        self.driver.find_element_by_xpath(self.password_path).send_keys(password)
        self.driver.find_element_by_xpath(self.login_button_path).click()

class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.payoff_path = "//body/app-root[1]/app-container-page[1]/div[1]/app-homepage[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/select"
        self.home_path ="//button[contains(text(),'New Trade')]"

    def select_payoff(self,payoff):
        self.driver.find_element_by_xpath(self.payoff_path).send_keys(payoff)

    def enter_payoff(self):
        self.driver.find_element_by_xpath(self.home_path).click()


