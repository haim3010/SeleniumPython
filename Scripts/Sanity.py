from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Selenium.Pages.sanity import Sanity
from Selenium.Pages.login import LoginPage
from Selenium.Pages.login import HomePage
from Selenium.Pages.NewRFQ import Create_RFQ
from selenium.webdriver.chrome.options import Options
import csv
import time
from datetime import date
import configparser
import logging
import sys
import unittest

today = date.today()

#mainDir = 'C:\\deployment\\SanityApi\\powershell\\Selenium\\'# -- server

mainDir = 'C:\\Users\\Haim\\PycharmProjects\\SeleniumProject\\Selenium\\'  # --- localy

print('\n====================================================\n'
      '================= START OF PROCESS =================\n'
      '====================================================\n')

logging.basicConfig(filename=mainDir + 'logs\\' + f'Sanity{today}.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info

configParser = configparser.RawConfigParser()
configFilePath = mainDir + 'files\\config.cfg'
configParser.read(configFilePath)

URL = str(configParser.get('Sanity', 'URL'))
UserName = str(configParser.get('Sanity', 'UserName'))
Password = str(configParser.get('Sanity', 'Password'))

counter = 3
sum_RFQs = 0

options = Options()
options.headless = True

with open(mainDir + 'files\\Selenium.csv', 'r') as csv_file:
    csv_read = csv.reader(csv_file)
    header = next(csv_read)
    if header != None:
        for line in csv_read:

            driver = webdriver.Chrome(executable_path=mainDir + 'Driver\\chromedriver.exe',options=options)
            driver.implicitly_wait(5)
            actions = ActionChains(driver)
            driver.get(URL)
            driver.maximize_window()

            login = LoginPage(driver)
            login.login(UserName, Password)
            time.sleep(2)

            homepage = HomePage(driver)
            driver.implicitly_wait(5)
            time.sleep(7)
            homepage.select_payoff(line[0])
            driver.implicitly_wait(30)
            homepage.enter_payoff()
            driver.implicitly_wait(20)

            sanity = Sanity(driver)
            sanity.Amount(line[1])
            driver.implicitly_wait(10)
            sanity.Solvefor(line[2])
            time.sleep(7)
            sanity.Underlyng(line[counter])
            time.sleep(2)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.perform()
            actions.send_keys(Keys.ENTER)
            actions.perform()
            driver.implicitly_wait(30)

            createRfq = Create_RFQ(driver)
            try:
                createRfq.Reload_rfq()
                time.sleep(2)
            except:
                pass
            driver.implicitly_wait(30)
            createRfq.Send_rfq()
            time.sleep(10)

            sum_RFQs = sum_RFQs + 1
            print(f"RFQ number f'{sum_RFQs} has been created")
            driver.close()
            driver.quit()

print("test completed")
