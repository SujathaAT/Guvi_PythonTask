import pandas as pd
from datetime import datetime


def get_test_steps(file_path):

    df = pd.read_excel(file_path, sheet_name="orangehrm_teststeps")
    return df.to_dict(orient='records')


def get_login_data(file_path):

    df = pd.read_excel(file_path, sheet_name="Result")
    return df.to_dict(orient='records')


def update_excel_result(file_path, test_id, username, status):

    df = pd.read_excel(file_path, sheet_name="Result")
    now = datetime.now()

    mask = (df['Test_id'] == test_id) & (df['Username'] == username)

    df.loc[mask, 'Date'] = now.strftime("%Y-%m-%d")
    df.loc[mask, 'Time'] = now.strftime("%H:%M:%S")
    df.loc[mask, 'Result'] = status

    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Result", index=False)
