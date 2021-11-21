import win32com.client
import time
import os
from easydict import EasyDict
from pywinauto import application
from util import load_config

class Connection:

    def __init__(self):
        self.objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")

    #### 연결여부 확인
    def check_connection(self):

        error_msg = "PLUS가 정상적으로 연결되지 않음."
        connect_msg = "PLUS가 정상적으로 연결됨."
        bConnect = self.objCpCybos.IsConnect

        if bConnect == 0:
            print(error_msg)
            return False

        else:
            print(connect_msg)
            return True
    
    #### 자동로그인, 모의투자는 자동로그인이 되지 않음
    def auto_login(self, maximum_try_num = 10):

        login_try_num = 0
        config_info = EasyDict(load_config())

        before_connection =  self.check_connection()

        if not before_connection:

            self.kill_client()

            id = config_info.creon_id
            pwd = config_info.creon_password
            pwdcert = config_info.certify_password

            app = application.Application()
            app.start('C:\\CREON\\STARTER\\coStarter.exe /prj:cp /id:{id} /pwd:{pwd} /pwdcert:{pwdcert} /autostart'.format(
                id=id, pwd=pwd, pwdcert=pwdcert))
            
            time.sleep(40)

        after_connection = self.check_connection()

        while not after_connection:

            if login_try_num > maximum_try_num:

                print("Fail login")
                
                return False

            time.sleep(1)
            login_try_num += 1

        print("Success login")

        return True

    #### 프로그램 종료
    def kill_client(self):
        os.system('taskkill /IM coStarter* /F /T')
        os.system('taskkill /IM CpStart* /F /T')
        os.system('taskkill /IM DibServer* /F /T')
        os.system('wmic process where "name like \'%coStarter%\'" call terminate')
        os.system('wmic process where "name like \'%CpStart%\'" call terminate')
        os.system('wmic process where "name like \'%DibServer%\'" call terminate')
