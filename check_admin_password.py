import paramiko
import re
import sys


def get_admin_pw():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'sqlite3 KHN-893NA/data/data/com.kocom.rndsw.kc_configservice/KC_Config.db "SELECT * FROM KC_CFG_PASSWORD_TB;"'
    (stdin, stdout, stderr) = ssh.exec_command(cmd)

    output = stdout.readline()

    pw_list = ("".join(output)).split('|')
    admin_pw = pw_list[1]  # 관리자 패스워드 얻어오기
    return admin_pw


def check_admin_pw_security(admin_pw, user_input):
    if(admin_pw == user_input):
        # 사용자가 입력한 관리자 패스워드와 월패드 내부의 db값과 같으면 -> 암호화가 안되어 있는 것
        return 0  # unsafe
    else:
        return 1  # safe


user_input = "56266"  # 툴에서 입력받은 사용자 입력 값 (전역변수로 넘겨받는 변수)
admin_pw = get_admin_pw()
result = check_admin_pw_security(admin_pw, user_input)
print("result(0->unsafe, 1->safe): ", result)
