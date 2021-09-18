import os
from pathlib import Path

class ConfigData:

    DOWNLOADS_PATH = str(Path.home() / "Downloads")+"\\"
    
    TESTDATA_EXCEL_PATH = os.getcwd()+"\\TestData\\TestData.xlsx"
    YUGASATESTREPORT_EXCEL_PATH = os.getcwd()+"\\TestRunner.xlsx"
    SLOTS_DOWNLOAD_JSON_FILE_PATH = DOWNLOADS_PATH + 'slot.json'                                                           
    SLOTS_FILE_UPLOAD_PATH = os.getcwd()+"\\TestData\\newslot.json"


    browserName = 'chrome'
    BASE_URL = "https://admin.helloyubo.com/login"
    COMMUNICATION_DOWNLOAD_CSV_FILE_PATH = DOWNLOADS_PATH+'leads.xlsx'
    INTENT_DOWNLOAD_CSV_FILE_PATH = DOWNLOADS_PATH+'Intents.xlsx'
    FALLBACKS_DOWNLOAD_CSV_FILE_PATH = DOWNLOADS_PATH+'fallback.xlsx'
    INTENT_FILE_UPLOAD_PATH = os.getcwd()+"\\TestData\\intents.json"
    EDITPROFILE_PROFILE_PIC_PATH = os.getcwd()+"\\TestData\\TestImage.png"
    SCREENSHOTS_FOLDER= os.getcwd()+"\\Reports\\Screenshots\\"