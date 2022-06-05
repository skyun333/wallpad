import paramiko
import re
import sys

# 사용자에게 입력 받을 mac주소 / 임시로 넣음
mac_addr = "00-15-31-30-61-8E"


def get_mac_addr():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'sqlite3 KHN-893NA/data/data/com.kocom.rndsw.kc_configservice/KC_Config.db "SELECT * FROM KC_CFG_IPCONFIG_TB;"'
    (stdin, stdout, stderr) = ssh.exec_command(cmd)

    output = stdout.readline()
    # 읽은 값 '|'로 구분하여 split하여 리스트로 반환받음
    # 현재 DB에 저장되어 있는 address 총 6개로 address_list의 크기는 6
    address_list = ("".join(output)).split('|')

    # ipconfig에 들어있는 \n 지우기
    for index, addr in enumerate(address_list):
        address_list[index] = addr.strip('\n')

    global mac_addr

    # mac_addr(전역변수)가 address_list에 있는지 확인 / 있으면 1, 없으면 0
    if mac_addr in address_list:
        return 1
    else:
        return 0

    ssh.close()


def return_res():
    result = get_mac_addr()
    return result
