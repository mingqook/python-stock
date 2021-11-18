import win32com.client

# 연결 여부 체크
def check_connection():

    error_msg = "PLUS가 정상적으로 연결되지 않음."
    connect_msg = "PLUS가 정상적으로 연결됨."

    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect

    if (bConnect == 0):
        print(error_msg)
        return False

    else:
        print(connect_msg)
        return True