import json
import win32com.client
import pandas as pd


def load_config():

    with open("config.json", "r") as f:

        return json.load(f)

def stock_name_to_code(stock_name_list):
    
    CpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

    return [CpStockCode.NameToCode(stock_name) for stock_name in stock_name_list]

def stock_name_list():

    return pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]['회사명']

def stock_code_list():

    return pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]['종목코드'].map('{0:0>6}'.format)

