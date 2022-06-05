import paramiko
import re
import sys


def get_pw():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'sqlite3 KHN-893NA/data/data/com.kocom.rndsw.kc_configservice/KC_Config.db "SELECT * FROM KC_CFG_PASSWORD_TB;"'
    (stdin, stdout, stderr) = ssh.exec_command(cmd)

    output = stdout.readline()
    # 읽은 값 '|'로 구분하여 split하여 리스트로 반환받음
    # 현재 DB에 저장되어 있는 password는 총 4개로 pw_list의 크기는 4
    pw_list = ("".join(output)).split('|')

    # 비밀번호에 들어있는 \n 지우기
    for index, pw in enumerate(pw_list):
        pw_list[index] = pw.strip('\n')

    # 리스트내애 있는 설정된 password를 정규표현식으로 검사
    # 최소 8자, 하나 이상의 문자, 하나의 숫자 및 하나의 특수 문자 정규식
    # 이부분은 월패드라는 점을 고려하여 수정가능
    for pw in pw_list:
        REGEX_PASSWORD = '^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{8,}$'
        flag = re.fullmatch(REGEX_PASSWORD, pw)
        # 정규식 검사를 통해 4개중 1개라도 위 정규식대로 구성되지 않았다면 False 반환
        if flag == 'None':
            ssh.close()
            return 0

    ssh.close()
    return 1


def return_res():
    result = get_pw()
    return result
