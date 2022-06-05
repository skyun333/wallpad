import paramiko
import re
import sys


def get_reboot_msg():  # reboot message 리스트 형태로 읽어 들이는 함수
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'cat KHN-893NA/data/system/wallpad_reboot.txt'
    (stdin, stdout, stderr) = ssh.exec_command(cmd)

    reboot_msg = stdout.readlines()
    return reboot_msg


def get_kernel_version(reboot_msg):  # reboot message에서 linux kernel 버전 얻는 함수
    for i in range(len(reboot_msg)):
        if("Restarting Linux version" in reboot_msg[i]):
            linux_kernel_version = (reboot_msg[i][40:46])
    return linux_kernel_version


# 해당 linux kernel 버전을 체크하여 보안성이 확보된 버전인지 확인하는 함수
def check_kernel_version(linux_kernel_version):
    if(linux_kernel_version < "5.17"):
        return 0
    else:
        return 1


def return_res():
    reboot_msg = get_reboot_msg()
    linux_kernel_version = get_kernel_version(reboot_msg)

    result = check_kernel_version(linux_kernel_version)
    #print("result(0->unsafe, 1->safe): ", result)
    return result
