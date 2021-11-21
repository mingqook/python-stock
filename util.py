import json
import win32com.client


def load_config():

    with open("config.json", "r") as f:

        return json.load(f)

def stock_name_to_code(stock_name_list):
    
    CpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

    return [CpStockCode.NameToCode(stock_name) for stock_name in stock_name_list]

