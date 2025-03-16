from googleapiclient.discovery import build
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#получение значение из поля гугл таблицы
def get_value_from_sheet():
    scopes = ['ссылка на таблицу']

    creds = service_account.Credentials.from_service_account_file(
        'ключ', scopes=scopes)

    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = 'id_таблицы'  

    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:A1'
    ).execute()


    values = response.get('values', [])
    if values:
        field_values = values[0]
        return field_values
    else:
        return 'Не удалось получить данные из Google Таблицы.'

#ввод значения в таблицу
def input_value_sheet(date):
    scopes = ['ссылка на таблицу']
    creds = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', scopes)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("ID таблицы").sheet1
    sheet.update_cell(1, 2, date)