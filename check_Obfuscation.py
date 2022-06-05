#-*- coding: utf-8 -*-
import paramiko
import re
import sys
from filecmp import cmp

def file_upload(remote_path, local_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'find -name '+ remote_path

    (stdin, stdout, stderr) = ssh.exec_command(cmd)
    output = stdout.readlines()


    remotepath1 = str(output)
    remotepath1 = remotepath1[3:len(remotepath1)-4]


    remotepath1 = "/root" + remotepath1
    localpath1 = './/'+local_path
    sftp = ssh.open_sftp()
    sftp.get(remotepath1,localpath1)
    ssh.close()
    
    return localpath1

def cmp_file(path1,path2):
    #������ ��ȣȭ �ȵ� ->  result = 1(False) / �ٸ��� ��ȣȭ �� -> result = 0(True)
    result = cmp(path1,path2)
      
    if result == 0:
        return 1
    else:
        return result

def return_res():
    svc1_r = '"svc1.txt"'
    svc1_l = "svc1.txt"
    svc2_r = '"svc2.txt"'
    svc2_l = "svc2.txt"
            
    path_svc1 = file_upload(svc1_r,svc1_l)
    path2_svc2 = file_upload(svc2_r,svc2_l)

    result = cmp_file(path_svc1,path2_svc2)
    return result
    
    