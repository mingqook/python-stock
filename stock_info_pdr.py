import pandas_datareader as pdr
from datetime import datetime
from util import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class StockInfoPdr:

    def __init__(self, kor_stock = None, startdate = None, enddate = None, source = None):

        if kor_stock == None:
            self.kor_stock = '005930'
        else:
            self.kor_stock = kor_stock

        if startdate == None:
            self.startdate = datetime(2021, 1, 1).strftime("%Y-%m-%d")
        else:
            self.startdate = startdate

        if enddate == None:
            self.enddate = datetime.today().strftime("%Y-%m-%d")
        else:
            self.enddate = enddate

        if source == None:
            self.source = 'naver'
        else:
            self.source = source

    def kor_stock_chart_info(self):

        stock_name = stock_name_list()
        stock_code = stock_code_list()

        if self.kor_stock.isdigit():

            if stock_code.isin([self.kor_stock]).any() :

                return pdr.DataReader(self.kor_stock, self.source, self.startdate, self.enddate)
            
            elif not stock_code.isin([self.kor_stock]).any():

                print("stock code 6자리를 제대로 입력하세요")
                exit()

        else:
            if stock_name.isin([self.kor_stock]).any():

                kor_stock_code = stock_name_to_code([self.kor_stock])  #### stock_name_to_code는 list를 출력 - but 여기서는 1개만 가정
                kor_stock_code = kor_stock_code[0][1:] #### "CREON API의 맨 앞 코드인 A를 제거"
                
                return pdr.DataReader(kor_stock_code, self.source, self.startdate, self.enddate)

            else:

                print("stock name을 제대로 입력하세요")
                exit()


    def stock_candle_html_save(self):
        
        chart_data = self.kor_stock_chart_info()
        
        #### 여러개의 plot을 한 번에 그림
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.03, subplot_titles=('Candle', 'Volume'), 
               row_width=[0.2, 0.7])

        # Plot OHLC on 1st row
        fig.add_trace(go.Candlestick(x = chart_data.index, open = chart_data['Open'], high = chart_data['High'], 
        low = chart_data['Low'], close = chart_data['Close'], name="Candle"), 
                row=1, col=1)

        # Bar trace for volumes on 2nd row without legend
        fig.add_trace(go.Bar(x = chart_data.index, y=chart_data['Volume'], showlegend=False), row=2, col=1)

        # Do not show Candle's rangeslider plot 
        fig.update(layout_xaxis_rangeslider_visible=False)

        fig.write_html('{0}_{1}~{2}.html'.format(self.kor_stock, self.startdate, self.enddate))