import win32com.client
import pandas as pd

#### https://github.com/lyy9257/Flask-KoreaStockBroker/blob/main/daishin/account_info_D.py
class AccountInfo:
    
    def __init__(self):

        self.CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
        self.CpTd6033 = win32com.client.Dispatch("CpTrade.CpTd6033")
        self.initCheck = self.CpTdUtil.TradeInit()

    def basic_account_info(self, request_num = 10):

        account_info_result = dict()
        account_num_list = [account_num for account_num in self.CpTdUtil.AccountNumber]
        
        
        for account_num in account_num_list:
            
            account_info = dict()
            stock_flag = self.CpTdUtil.GoodsList(account_num,1) #### 계좌 내 주식 관련 정보 filtering(????) -> -1을 넣으면 list 원소 3개 생김

            self.CpTd6033.SetInputValue(0, account_num)
            self.CpTd6033.SetInputValue(1, stock_flag[0])
            self.CpTd6033.SetInputValue(2, request_num) #### 요청건수 / 최대 50개
            self.CpTd6033.SetInputValue(3, '2') #### 수익률 0%기준

            self.CpTd6033.BlockRequest()

            account_info['계좌명'] = self.CpTd6033.GetHeaderValue(0)
            account_info['총 평가금액'] = self.CpTd6033.GetHeaderValue(3)
            account_info['평가손익'] = self.CpTd6033.GetHeaderValue(4)
            account_info['수익률'] = self.CpTd6033.GetHeaderValue(8)
            account_info['D+2 예상예수금'] = self.CpTd6033.GetHeaderValue(9)

            account_info_result['계좌번호_{}'.format(account_num)] = account_info

        
        return account_info_result

    def account_stock_info(self, request_num = 10):

        account_info_result = dict()
        account_num_list = [account_num for account_num in self.CpTdUtil.AccountNumber]
        stock_info_name_list = ['종목명', '종목코드', '체결장부단가', '평가금액',  '평가손익', '수익률', '결제잔고수량', '체결잔고수량']
        stock_info_idx_list = [0, 12, 17, 9, 10, 11, 3, 7]
        
        for account_num in account_num_list:
            
            stock_info_df = pd.DataFrame(columns=stock_info_name_list)
            stock_flag = self.CpTdUtil.GoodsList(account_num,1)

            self.CpTd6033.SetInputValue(0, account_num)
            self.CpTd6033.SetInputValue(1, stock_flag[0])
            self.CpTd6033.SetInputValue(2, request_num) #### 요청건수 / 최대 50개
            self.CpTd6033.SetInputValue(3, '2') #### 수익률 0%기준

            self.CpTd6033.BlockRequest()

            account_stock_num = self.CpTd6033.GetHeaderValue(7)
            temp_stock_info_df = pd.DataFrame(columns=stock_info_name_list)

            for k in range(len(stock_info_name_list)):

                stock_info_idx = stock_info_idx_list[k]
                temp_stock_info = [self.CpTd6033.GetDataValue(stock_info_idx, stock_idx) for stock_idx in range(account_stock_num)]
                temp_stock_info_df[stock_info_name_list[k]] = temp_stock_info            

            stock_info_df = pd.concat([stock_info_df, temp_stock_info_df]).reset_index(drop = True)

            account_info_result['계좌번호_{}'.format(account_num)] = stock_info_df

        return account_info_result