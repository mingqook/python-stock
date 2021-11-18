# CREON API(대신증권 API) 

* 출처 :  https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_List_Page.aspx?boardseq=284&m=9505&p=8841&v=8643

* CREON API는 C언어로 작성되어 제공된다. 

* python에서 C언어로 작성된 객체를 사용하기 위해 win32com.client.Dispatch('객체명')을 활용한다.

* CYBOS Code 규칙

  * | 분류     | 내용                | CYBOS의비교화면                    |
    | -------- | ------------------- | ---------------------------------- |
    | 주식     | A + 6자리(A003540)  | tr7021,7024 등등의주식화면         |
    | ETN      | Q + 6자리(Q500001)  | 7021, 7024 등의 주식 화면          |
    | 업종     | U + 3자리 (U001)    | tr7036,7035,7041,7042 등의업종화면 |
    | Elw      | J + 6자리 (J506633) | tr7714,8971 등의 elw화면           |
    | 선물옵션 | CYBOS와동일함       |                                    |



## 1. 국내 주식 정보 관련 API

#### 1.1 CpUtil.CpCybos

* CYBOS의 상태를 확인
* value = object.**IsConnect**
  * (읽기전용) CYBOS의통신연결상태를반환합니다 -> 반환값 : 0 - 연결끊김, 1 - 연결정상
* value = object.**LimitRequestRemainTime**
  * 요청개수를재계산하기까지남은시간을반환합니다. 

#### 1.2  CpUtil.CpStockCode

* CYBOS에서 사용되는 주식코드 조회 작업 수행
* value = object.**CodeToName(code)**
  * code에 해당하는 종목명을 반환
  * code : 종목코드 
* value = object. **NameToCode(name)**
  * name에 해당하는 종목코드를 반환
* value = object.**CodeToFullCode(code)**
  * code에 해당하는 FullCode를 반환
  * code : 종목코드
* value = object.**FullCodeToName(fullcode)**
  * fullcode에 해당하는 종목명을 반환
* value = object. **CodeToIndex(code)**
  * code에 해당하는 Index를 반환
* value = object.**GetCount()**
  * 종목코드 수를 반환
* value = object.**GetData(type,index)**
  * 해당 인덳의 종목 데이터를 구한다. 
  * type : 데이터 종류
    * 0 - 종목코드 
    * 1 - 종목명
    * 2 - full code
  * index  : 종목코드 인덱스 
* value = object.**GetPriceUnit(code, basePrice, directionUp)**
  * 주식/ETF/ELW의 호가 단위를 구한다.
  * code : 종목코드 / basePrice : 기준가격 / directionUp : 상승의 단위인가의 여부 

#### 1.3 CpUtil.CpCodeMgr

* 각종 코드 정보 및 코드리스트를 얻을 수 있음
* value = object.**CodeToName**( code )
  * code에 해당하는 주식/선물/옵션 종목명을 반환
* value = object.**GetStockIndustryCode** ( code )
  * code에 해당하는 증권 전산 업종코드를 반환
* value = object.**GetStockKospi200Kind** ( code )
  * code에 해당하는 KOSPI200 종목 여부를 반환
* value = object.**GetStockSectionKind**( code )
  * code에 해당하는 부구분코드를 반환
* value = object.**GetStockStdPrice** ( code )
  * code에 해당하는 권리락 등으로 인한 기준가를 반환
* value = object.**GetStockYdOpenPrice** ( code )
  * code에 해당하는 전일시가를 반환
* value = object.**GetStockYdHighPrice** ( code )
  * code에 해당하는 전일고가를 반환
* value = object.**GetStockYdLowPrice** ( code )
  * code에 해당하는 전일저가를 반환
* value = object.**GetStockYdClosePrice** ( code )
  * code에 해당하는 전일종가를 반환
* value = object.**GetStockListByMarket**(CPE_MARKET_KIND code )
  * 시장구분에 따른 주식 종목 배열을 반환
    * CPE_MARKET_KIND code : 1 - 거래소 / 2 - 코스닥

#### 1.4 Dscbo1.StockMst

* 주식종목의 현재가에 관련된 데이터(10차 호가 포함)
* return을 얻기 이전에 반드시 Request 절차 필요 -  object.**Request()** / object.**BlockRequest()** 활용
* object.**SetInputValue(type,value)**
  * type에 해당하는 입력데이터를  value 값으로 지정
  * 기본적으로 type = 0, value = 종목코드 사용
* value = object.**GetHeaderValue(type**)
  * type에 해당하는 헤더 데이터를 반환
  * type 값 설명
    * 0 : 종목코드 / 1 : 종목명 / 2 : 대신업종코드 / 3 : 그룹코드 / 4 : 시간
    * 5 : 소속구분 / 6 : 대형,중형,소형 / 8 : 상한가 / 9 : 하한가 / 10 : 전일종가
    * 11 : 현재가 / 12 : 전일대비 / 13 : 시가 / 14 : 고가 / 15 : 저가
    * 16 : 매도호가 / 17 : 매수호가 / 20 : EPS / 21 : 연중최고가
    * 22 : 연중최고가 일자 / 23 : 연중최저가 / 24 : 연중최저가 일자
    * 28 : PER / 70 : BPS / 71 : 총매도잔량 / 73 : 총매수잔량
* value = object.**GetDataValue (Type,index)**
  * type에 해당하는 데이터를 반환
  * type 값 설명
    * 0 : 매도호가 / 1 : 매수호가 / 2 : 매도잔량 / 3 : 매수잔량 / 4 : 매도잔량대비 / 5 : 매수잔량대비
* object.**Request()**
  * 종몽코드의 현재가 관련 데이터를 요청
* object.**BlockRequest()**
  * 데이터요청 / Blocking Mode
  * 기본 Request()보다 주로 사용하는듯

#### 1.5 Dscbo1.StockCur

* 주식 / 업종 / ELW 시세 데이터를 수신
* Dscbo1.StockMst 객체와 사용법은 유사
* return을 얻기 이전에 반드시 Request 절차 필요 -  object.**Request()** / object.**BlockRequest()** 활용
* object.**SetInputValue(type,value)**
* value = object.**GetHeaderValue(type)**

#### 1.6 Dscbo1.StockWeek

* 주식종목에대해 일자별 주가데이터(최고 10년치)를 최근 날로부터 일정 시점까지 시가, 고가, 저가, 종가 등 정보 제공
* return을 얻기 이전에 반드시 Request 절차 필요 -  object.**Request()** / object.**BlockRequest()** 활용

#### 1.7 Dscbo1.StockAdR

* 거래소 등락 현황 데이터(상승, 상한, 하한 종목수 등) 요청 및 수신
* return을 얻기 이전에 반드시 Request 절차 필요 -  object.**Request()** / object.**BlockRequest()** 활용
* value = object.**GetHeaderValue(type)**
  * type 값 설명
    * 0 : 상승종목수 / 1 : 상한종목수 / 2 : 보합종목수 / 3 : 하락종목수 / 4 : 하한종목수
    * 5 : 지수 / 6 : 지수전일대비

#### 1.8 Dscbo1.StockAdKR

* 코스닥 당락 현황 데이터(상승, 상한, 하한 종목수 등) 요청 및 수신
* Dscbo1.StockAdR와 사용방법 동일

#### 1.9 CpSysDib.MarketEye

* 주식, 지수, 선물/옵션 등의 여러 종목의 필요한 항목들을 한 번에 수신
* object.**SetInputValue(type,value)**
  * type에 해당하는 입력 데이터를 value 값으로 지정
  * 아래 예시를 보는 것이 활용 방법 파악에 있어 용이 
    *  https://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_Read.aspx?boardseq=299&seq=45&page=2&searchString=&prd=&lang=7&p=8833&v=8639&m=9505



## 2. 계좌  / 주문 관련 API

#### 2.1 CpTrade.CpTdUtil

* 주문오브젝트를 사용하기 위해 필요한 초기화과정들을 수행
* 모든 주문오브젝트를 사용하기 전에, **필수적으로 TradeInit을 호출** 한 후에 사용할 수 있다. 
* 전역변수로 선언하여 사용해야 함
* Value = object.**TradeInit(Reserved)**
  * 주문을 하기 위한 예비과정을 수행
  * Reserved는 0을 default로 설정
  * Return : -1 : 오류 / 0 : 정상 / 1 : OTP, 보안카드 키 입력 오류 / 3 : 취소
* Value = Object.**AccountNumber** (읽기전용)
  * TradeInit을 정상적으로 수행한 이후 얻을 수 있음
  * 계좌목록을 반환
* Value = Object.**GoodsList**(string sAcc,int nFilter)
  * TradeInit을 정상적으로 수행한 이후 얻을 수 있음
  * 사인온 한 계좌에 대해서 필터값에 따른계좌 목록을 배열로 반환
  * string sAcc - 계좌번호
  * int nFilter 
    * -1 : 전체 / 1 : 주식 / 2 : 선물, 옵션 / 3 : 주식(1) + 선물/옵션(2)

#### 2.2 CpTrade.CpTd0311

* 장내주식, 코스닥 주식, ELW의 현금주문 데이터를 요청하고 수신
* object.**SetInputValue(type,value)**
  * type에 해당하는 입력데이터를 value 값으로 지정
  * type 값 설명
    * 0 : 주문종류코드 -> value(string) : 1 - 매도 / 2 - 매수
    * 1 : 계좌번호
    * 2 : 상품관리구분코드
    * 3 : 종목코드
    * 4 : 주문수량
    * 5 : 주문단가
    * 8 : 주문호가구분코드 -> value(string) : 01 - 보통(default) / 02 : 임의 / 03 : 시장가 / 12 : 최유리지정가 / 13 : 최우선지정가
* object.**BlockRequest()**
  * hts 장내 주식 현금 주문관련 데이터 요청
  * 주문을 요청하는 과정

#### 2.3 CpTrade.CpTd0313

* 장내주식, 코스닥 주식, ELW의 가격정정주문 데이터를 요청하고 수신

#### 2.4 CpTrade.CpTd0314

* 장내주식, 코스닥 주식, ELW의 취소주문 데이터를 요청하고 수신

#### 2.5 CpTrade.CpTd6033

* 계좌별 잔고 및 주문 체결 평가 현황 데이터를 요청하고 수신
* 주식 이외의 상품에 대한 평가금액과 예수금 변동은 포함되어 있지 않음에 유의
* object.**SetInputValue(type,value)**
  * type 값 설명
    * 0 : 계좌번호 / 1 : 상품관리구분코드 / 2 : 요청건수 - 최대 50개, default 14개 / 3 : 수익률구분코드 - "1" : 100프로 기준, "2" : 0프로 기준
* value = object.**GetHeaderValue(type**)
  * type 값 설명
    * 0 : 계좌명 / 1 : 결제잔고수량 / 2 : 체결잔고수량 / 3 : 총 평가금액 / 4 : 평가손익 / 8 : 수익률
    * 9 : D+2 예상 예수금
* value = object.**GetDataValue(Type,Index)**
  * Ttype 값 설명
    * 0 : 종목명
    * 1 : 신용구분 -> value(string) : 'Y' - 신용융자, 유통유자 /  'D' - 신용대주 / 유통대주
    * 2 : 대출일
    * 3 : 결제잔고수량
    * 5 : 전일 체결수량 / 6 : 금일 체결량
    * 9 : 평가금액 / 10 : 평가손익 / 11 : 수익률 / 12 : 종목코드 / 15 : 매도가능수량 / 18 : 손익단가
* object.**BlockRequest()**
  * data 요청