import win32com.client
import os

# test = win32com.client.Dispatch("CpSysDib.MarketEye")
# CpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# print(test.CodeToName('A005930'))
# print(test.CodeToIndex('A005930'))
# test.SetInputValue(0, [0,17,1,2,3,4,5])
# test.SetInputValue(1, ["A003540", "A000660", "A005930", "A035420", "A069500", "Q530031"])
# test.BlockRequest()
# print(test.GetDataValue(6,1))

# print(CpStockCode.NameToCode('삼성전자'))


# test = win32com.client.Dispatch("Dscbo1.StockMst")
# test.SetInputValue(0, 'A005930')
# test.BlockRequest()
# print(test.GetHeaderValue(11))
# print(test.GetHeaderValue(13))
# print(test.GetHeaderValue(14))
# print(test.GetHeaderValue(15))

# print(os.system('tasklist'))

test = win32com.client.Dispatch('CpTrade.CpTdUtil')
test.TradeInit()
print(test.AccountNumber)

test2 = win32com.client.Dispatch('CpTrade.CpTd6033')
test2.SetInputValue(0, test.AccountNumber[0])
print(test2.GetHeaderValue(3))



# import win32com.client
 
# # 종목코드 리스트 구하기
# objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# codeList = objCpCodeMgr.GetStockListByMarket(1) #거래소
# codeList2 = objCpCodeMgr.GetStockListByMarket(2) #코스닥
 
 
# print("거래소 종목코드", len(codeList))
# for i, code in enumerate(codeList):
#     secondCode = objCpCodeMgr.GetStockSectionKind(code)
#     name = objCpCodeMgr.CodeToName(code)
#     stdPrice = objCpCodeMgr.GetStockStdPrice(code)
#     print(i, code, secondCode, stdPrice, name)
 
# print("코스닥 종목코드", len(codeList2))
# for i, code in enumerate(codeList2):
#     secondCode = objCpCodeMgr.GetStockSectionKind(code)
#     name = objCpCodeMgr.CodeToName(code)
#     stdPrice = objCpCodeMgr.GetStockStdPrice(code)
#     print(i, code, secondCode, stdPrice, name)
 
# print("거래소 + 코스닥 종목코드 ",len(codeList) + len(codeList2))