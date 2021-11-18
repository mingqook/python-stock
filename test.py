import win32com.client

# test = win32com.client.Dispatch("CpSysDib.MarketEye")
CpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# print(test.CodeToName('A005930'))
# print(test.CodeToIndex('A005930'))
# test.SetInputValue(0, [0,17,1,2,3,4,5])
# test.SetInputValue(1, ["A003540", "A000660", "A005930", "A035420", "A069500", "Q530031"])
# test.BlockRequest()
# print(test.GetDataValue(6,1))

print(CpStockCode.NameToCode('삼성전자'))