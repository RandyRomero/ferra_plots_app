"""
Module that connects to a particular google spreadsheet with results of
smartphones benchmarks return one sheet from a table
"""
from typing import List

# It works irregardless pycharm's whining
from apiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

import app_config as cfg

def get_spreadsheet(sheet_name: str) -> List[List[str]]:

    """
    Connects to a particular google spreadsheet with results of
    smartphones benchmarks return one sheet from a table

    :param sheet_name: str with a name of a sheet which contains results of
    smartphones in one particular benchmark
    :return: list of lists where every list represents one row of a table
    """

    scopes = ['https://spreadsheets.google.com/feeds',
              'https://www.googleapis.com/auth/drive']

    cred_file = cfg.GOOGLE_CREDENTIAL_FILE
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scopes)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    gsheet = service.spreadsheets().values().get(
        spreadsheetId=cfg.SPREADSHEET_ID, range=sheet_name).execute()

    print(gsheet)
    return gsheet['values'][2:]

