import pyodbc
import pandas as pd
import textwrap
import openpyxl
import configparser



from datetime import date
today = date.today()

mainDir = 'C:\\Users\\haim\\PycharmProjects\\SeleniumProject\\Selenium\\files\\'


configParser = configparser.RawConfigParser()
configFilePath = mainDir + 'config.cfg'
configParser.read(configFilePath)

DBname = configParser.get('DB','DBname')
serverdb = configParser.get('DB','serverdb')


con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      f"Server={serverdb};"
                      f"Database={DBname};"
                      "Trusted_Connection=no;"
                      "uid=sa;pwd=6six66")

def create_string(sql_full_path):
    with open(sql_full_path, 'r') as f_in:
        lines = f_in.read()
        # remove any common leading whitespace from every line
        query_string = textwrap.dedent("""{}""".format(lines))

    return query_string

path = 'C:\\Users\\haim\\hai\\' + 'heatmap.sql'

query_parse = create_string(path)

query_execute = pd.read_sql_query(query_parse, con)

dbDataDF = pd.DataFrame(query_execute)

#tips[(tips['time'] == 'Day') & (tips['tip'] > 5.00)]

dbDataDF.to_excel('C:\\Users\\haim\\PycharmProjects\\SeleniumProject\\Selenium\\files\\sanity.xlsx',sheet_name='Sanity')


