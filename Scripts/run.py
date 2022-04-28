from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Selenium.Pages.login import LoginPage
from Selenium.Pages.login import HomePage
from Selenium.Pages.Autocall import Payoff_autocall
from Selenium.Pages.RFQ import Create_RFQ
import pandas as pd
import csv
import time
import openpyxl
import logging
import sys
#import datetime
from datetime import date
import configparser
#import xlrd
#import openpyxl
today =date.today()
sum_RFQs=0
counter=9
from selenium.webdriver.chrome.options import Options

#mainDir = 'C:\\deployment\\SanityApi\\powershell\\Selenium\\'# -- server


mainDir = 'C:\\Users\\Haim\\PycharmProjects\\SeleniumProject\\Selenium\\'# --- localy

logging.basicConfig(filename=mainDir +'logs\\' + f'Autocall{today}.log',
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

URL = str(configParser.get('Sanity', 'URL'))
UserName = str(configParser.get('Autocall', 'UserName'))
Password = str(configParser.get('Autocall', 'Password'))

AC_note = pd.read_excel( 'C:\\Users\haim\\PycharmProjects\\SeleniumProject\\Selenium\\files\\Autocall.xlsm', sheet_name='AutocallFinal') # read excel
AC_note.to_csv( mainDir+'files\\Autocall_RC.csv')
file_path = mainDir + 'files\\Autocall_RC.csv'

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
        homepage.select_payoff(rows[1])
        time.sleep(4)
        homepage.enter_payoff()
        driver.implicitly_wait(5)
        time.sleep(20)
        trade_details = Payoff_autocall(driver)
        time.sleep(5)
        trade_details.Name(rows[2])
        time.sleep(2)
        trade_details.Maturity(rows[4])
        time.sleep(2)
        trade_details.Currency(rows[5])
        time.sleep(2)
        trade_details.Amount(rows[6])
        time.sleep(2)
        trade_details.Autocall_Observation(rows[14])
        time.sleep(2)
        trade_details.Non_Autocall(rows[16])
        time.sleep(2)
        trade_details.Solvefor(rows[7])

        if rows[7]=='Coupon Per Period':
            trade_details.Reoffer(rows[25])
        else:
            trade_details.Coupon(rows[17])
        time.sleep(3)

        while rows[counter] != "":
          trade_details.Underlyng(rows[counter])
          time.sleep(2)
          actions.send_keys(Keys.ARROW_DOWN)
          actions.perform()
          actions.send_keys(Keys.ENTER)
          actions.perform()
          counter=counter+1
          if counter == 14:
            break

        time.sleep(2)
        trade_details.Downside_type(rows[20])
        trade_details.Knock_in_barrier_type(rows[23])
        time.sleep(2)
        trade_details.Knock_in_barrier(rows[24])
        time.sleep(5)
        trade_details.Create_RFQ()
        driver.implicitly_wait(5)
        time.sleep(10)

        createRfq = Create_RFQ(driver)
        createRfq.create_rfq()
        driver.implicitly_wait(30)
        try:
          createRfq.Reload_rfq()
        except:
          pass
        time.sleep(7)
        createRfq.Select_rfq()
        driver.implicitly_wait(30)
        createRfq.Send_rfq()
        driver.implicitly_wait(30)

        counter=9
        sum_RFQs=sum_RFQs+1
        driver.close()
        driver.quit()
        time.sleep(10)
        print(f"RFQ number f'{sum_RFQs} has been created")

print("test completed")
