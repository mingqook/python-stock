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

# test = win32com.client.Dispatch('CpTrade.CpTdUtil')
# test.TradeInit()
# # print(test.AccountNumber)
# acc_num_list = [num for num in test.AccountNumber]
# # print(acc_num_list)
# test2 = win32com.client.Dispatch('CpTrade.CpTd6033')
# test2.SetInputValue(0, acc_num_list[0])
# print(test.GoodsList(acc_num_list[0],-1)) #### 계좌 내 주식 관련 정보 filtering(????)
# test2.BlockRequest()
# print(test2.GetHeaderValue(4))



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


class StockInfo():

    ## 초기화
    def __init__(self):
        self.obj_CpSysDib_StockChart = win32com.client.Dispatch('CpSysDib.StockChart')
        self.obj_CpSysDib_MarketEye = win32com.client.Dispatch('CpSysDib.MarketEye')
        self.obj_CpSysDib_CpSvr7238 = win32com.client.Dispatch('CpSysDib.CpSvr7238')
        self.obj_CpSysDib_CpSvr7254 = win32com.client.Dispatch('CpSysDib.CpSvr7254')
        self.obj_CpSysDib_CpMarketEye = win32com.client.Dispatch('CpSysDib.MarketEye')
        self.obj_CbSysDib_CpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
        self.obj_CpTrade_CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
        self.obj_CpUtil_CpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
        self.obj_DsCbo1_StockMst = win32com.client.Dispatch("DsCbo1.StockMst")

        self.initCheck = self.obj_CpTrade_CpTdUtil.TradeInit(0)


    def get_stockfeatures(self,code):
        
        ## 1차 데이터 호출
        result = {
            '이름': self.obj_CpUtil_CpCodeMgr.CodeToName(code),
            '증거금률(%)': self.obj_CpUtil_CpCodeMgr.GetStockMarginRate(code),
            '시장구분코드 ': self.obj_CpUtil_CpCodeMgr.GetStockMarketKind(code),
            '부구분코드': self.obj_CpUtil_CpCodeMgr.GetStockSectionKind(code),
            '감리': self.obj_CpUtil_CpCodeMgr.GetStockControlKind(code),
            '관리': self.obj_CpUtil_CpCodeMgr.GetStockSupervisionKind(code),
            '현재상태': self.obj_CpUtil_CpCodeMgr.GetStockStatusKind(code),
            '결산기': self.obj_CpUtil_CpCodeMgr.GetStockFiscalMonth(code),
            'K200여부': self.obj_CpUtil_CpCodeMgr.GetStockKospi200Kind(code),
            '업종코드': self.obj_CpUtil_CpCodeMgr.GetStockSectionKind(code),
            '상장일': self.obj_CpUtil_CpCodeMgr.GetStockListedDate(code),
            '신용가능여부': self.obj_CpUtil_CpCodeMgr.IsStockCreditEnable(code),
        }

        ## 2차 데이터 입력값 설정
        _fields = [67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 86, 87, 88,
            89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111
        ]

        _keys = ['PER', 'EPS', '자본금(백만)', '액면가', '배당률', '배당수익률', '부채비율', '유보율',
            '자기자본이익률(ROE)', '매출액증가율', '경상이익증가율', '순이익증가율', '투자심리', '매출액',
            '경상이익', '당기순이익', 'BPS', '영업이익증가율', '영업이익', '매출액영업이익률', '매출액경상이익률',
            '이자보상비율', '분기BPS', '분기매출액증가율', '분기영업이익증가율', '분기경상이익증가율', '분기순이익증가율',
            '분기매출액', '분기영업이익', '분기경상이익', '분기당기순이익', '분기매출액영업이익률', '분기매출액경상이익률',
            '분기ROE', '분기이자보상비율', '분기유보율', '분기부채비율', '최근분기년월'
        ]

        self.obj_CpSysDib_MarketEye.SetInputValue(0, _fields)
        self.obj_CpSysDib_MarketEye.SetInputValue(1, code)
        self.obj_CpSysDib_MarketEye.BlockRequest()

        field_length = self.obj_CpSysDib_MarketEye.GetHeaderValue(0)

        if field_length > 0:
            for i in range(field_length):
                value = self.obj_CpSysDib_MarketEye.GetDataValue(i, 0)
                if type(value) == float:
                    value = round(value, 4)
                    
                result[_keys[i]] = value

        return result


s = StockInfo()
print(s.get_stockfeatures('A003540'))