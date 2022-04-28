from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Selenium.Pages.login import LoginPage
from Selenium.Pages.login import HomePage
from Selenium.Pages.up_out import UPNOUT
from Selenium.Pages.RFQ import Create_RFQ
import csv
import time
import logging
import sys
from datetime import date
import configparser

today =date.today()
sum_RFQs=0
counter=4
from selenium.webdriver.chrome.options import Options



#mainDir = 'C:\\deployment\\SanityApi\\powershell\\Selenium\\'# -- server


mainDir = 'C:\\Users\\Haim\\PycharmProjects\\SeleniumProject\\Selenium\\'# --- localy

logging.basicConfig(filename=mainDir +'logs\\' + f'up_out{today}.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info



print('\n====================================================\n'
      '================= START OF PROCESS =================\n'
      '====================================================\n')


configParser = configparser.RawConfigParser()
configFilePath = mainDir + 'files\\config.cfg'
configParser.read(configFilePath)

URL = str(configParser.get('UPNOUT', 'URL'))
UserName = str(configParser.get('UPNOUT', 'UserName'))
Password = str(configParser.get('UPNOUT', 'Password'))


file_path = mainDir + 'files\\up_out.csv'

options = Options()
options.headless = True

with open(file_path,'r') as csv_Autocall:
  csv_read = csv.reader(csv_Autocall)
  header = next(csv_read)
  if header!= None :
      for rows in csv_read:
        driver = webdriver.Chrome(mainDir + 'Driver\\chromedriver.exe')#,options=options)
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        driver.get(URL)
        driver.maximize_window()

        time.sleep(2)
        login = LoginPage(driver)
        login.login(UserName,Password)
        time.sleep(2)
        homepage = HomePage(driver)
        driver.implicitly_wait(5)
        time.sleep(7)
        homepage.select_payoff(rows[0])
        driver.implicitly_wait(30)
        homepage.enter_payoff()
        time.sleep(2)

        up_out = UPNOUT(driver)
        up_out.Amount(rows[1])
        up_out.Solvefor(rows[2])
        driver.implicitly_wait(30)
        time.sleep(2)

        while rows[counter] != "":
          up_out.Underlyng(rows[counter])
          time.sleep(2)
          actions.send_keys(Keys.ARROW_DOWN)
          actions.perform()
          actions.send_keys(Keys.ENTER)
          actions.perform()
          counter=counter+1
          if counter == 9:
            break

        time.sleep(3)
        up_out.Maturity(rows[9])
        driver.implicitly_wait(10)
        up_out.Participation(rows[10])
        up_out.Premium(rows[11])
        time.sleep(2)
        up_out.Barrier(rows[12])
        time.sleep(5)

        createRfq = Create_RFQ(driver)
        createRfq.create_rfq()
        time.sleep(3)
        try:
          createRfq.Reload_rfq()
        except:
          pass
        driver.implicitly_wait(30)
        createRfq.Select_rfq()
        driver.implicitly_wait(30)
        createRfq.Send_rfq()
        time.sleep(3)

        counter=4
        sum_RFQs=sum_RFQs+1
        driver.close()
        driver.quit()
        time.sleep(360)
        print(f"RFQ number f'{sum_RFQs} has been created")

print("test completed")

