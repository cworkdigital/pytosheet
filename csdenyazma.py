import requests
import re
from bs4 import BeautifulSoup
import json
import html
import pandas as pd
import openpyxl as xls
import time
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import gspread_dataframe as gd

import pandas as pd
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time
import schedule

def autowrite():

    scopes = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file(
        'C:\\Users\\Admin\\PycharmProjects\\creds.json', scopes=scopes)

    gc = gspread.authorize(credentials)

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    # open a google sheet
    gs = gc.open('scrapetosheets')
    # select a work sheet from its name
    worksheet1 = gs.worksheet('scrapetosheets')

    # dataframe (create or import it)
    # write to dataframe
    schedule.every(1).minute.do(worksheet1.clear)
    with open('dnm.csv', 'r', encoding="UTF-8") as file_obj:
        content = file_obj.read()
        gc.import_csv(gs.id, data=content)

schedule.every(1).minute.do(autowrite)
while True:
    schedule.run_pending()
    time.sleep(2)

group_link, var_urls, product_dt, pro_stk_info
