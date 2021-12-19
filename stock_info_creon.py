import win32com.client
import pandas as pd
from datetime import datetime


class StockInfoCreon:
    def __init__(self):

        self.obj_CpSysDib_MarketEye = win32com.client.Dispatch('CpSysDib.MarketEye')
        self.obj_CpTrade_CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
        self.obj_CpUtil_CpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
        self.obj_CpSysDib_StockChart = win32com.client.Dispatch('CpSysDib.StockChart')


        self.initCheck = self.obj_CpTrade_CpTdUtil.TradeInit(0)


    def get_stock_info(self,code):
        
        ## 1차 데이터 호출
        result = {
            '이름': self.obj_CpUtil_CpCodeMgr.CodeToName(code),
            '증거금률(%)': self.obj_CpUtil_CpCodeMgr.GetStockMarginRate(code),
            '시장구분코드 ': self.obj_CpUtil_CpCodeMgr.GetStockMarketKind(code),
            '부구분코드': self.obj_CpUtil_CpCodeMgr.GetStockSectionKind(code),
            '현재상태': self.obj_CpUtil_CpCodeMgr.GetStockStatusKind(code),
            '결산기': self.obj_CpUtil_CpCodeMgr.GetStockFiscalMonth(code),
            'K200여부': self.obj_CpUtil_CpCodeMgr.GetStockKospi200Kind(code),
            '업종코드': self.obj_CpUtil_CpCodeMgr.GetStockSectionKind(code),
            '상장일': self.obj_CpUtil_CpCodeMgr.GetStockListedDate(code),
            '신용가능여부': self.obj_CpUtil_CpCodeMgr.IsStockCreditEnable(code),
        }

        ## 2차 데이터 입력값 설정
        _fields = [67, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 86, 87, 88,
            89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 150, 158, 159, 160, 161, 162
        ]

        _keys = ['PER', 'EPS', '자본금(백만)', '액면가', '배당률', '배당수익률', '부채비율',
            '자기자본이익률(ROE)', '매출액증가율', '경상이익증가율', '순이익증가율', '매출액',
            '경상이익', '당기순이익', 'BPS', '영업이익증가율', '영업이익', '매출액영업이익률', '매출액경상이익률',
            '이자보상비율', '분기BPS', '분기매출액증가율', '분기영업이익증가율', '분기경상이익증가율', '분기순이익증가율',
            '분기매출액', '분기영업이익', '분기경상이익', '분기당기순이익', '분기매출액영업이익률', '분기매출액경상이익률',
            '분기ROE', '분기이자보상비율', '분기유보율', '분기부채비율', '최근분기년월', '베타계수', '5일전종가', '10일전종가',
            '20일전종가', '60일전종가', '120일전종가'
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


    def get_chart_info(self, code, unit='D', n=None, date_from=None, date_to=None):
            
        _fields = [0, 2, 3, 4, 5, 8, 9]
        _keys = ['date', 'open', 'high', 'low', 'close', 'volume', 'vol_amount']

        if date_to is None:
            date_to = datetime.today().strftime('%Y%m%d')

        ## 필요 데이터 입력
        self.obj_CpSysDib_StockChart.SetInputValue(0, code) # 주식코드: A, 업종코드: U

        if n is not None:
            self.obj_CpSysDib_StockChart.SetInputValue(1, ord('2'))  # 0: ?, 1: 기간, 2: 개수
            self.obj_CpSysDib_StockChart.SetInputValue(4, n)  # 요청 개수

        if date_from is not None or date_to is not None:
            if date_from is not None and date_to is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(1, ord('1'))  # 0: ?, 1: 기간, 2: 개수
            if date_from is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(3, date_from)  # 시작일
            if date_to is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(2, date_to)  # 종료일

        self.obj_CpSysDib_StockChart.SetInputValue(5, _fields)  # 필드
        self.obj_CpSysDib_StockChart.SetInputValue(6, ord(unit))
        self.obj_CpSysDib_StockChart.SetInputValue(9, ord('1')) # 0: 무수정주가, 1: 수정주가
        
        ## 호출
        self.obj_CpSysDib_StockChart.BlockRequest()

        length = self.obj_CpSysDib_StockChart.GetHeaderValue(3)
        list_item = []

        for i in range(length):
            temp_idx = []
            for j in range(len(_keys)):
                temp_idx.append(self.obj_CpSysDib_StockChart.GetDataValue(j, i))
            list_item.append(temp_idx)

        result = pd.DataFrame(data=list_item, columns=_keys).reset_index()

        return result.loc[:, "date":]