#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
python 3.6.3 远程连接linux并执行命令
'''

# 导入模块
import paramiko
def con_linux(hostname, username, password):
    s = paramiko.SSHClient()
    # 取消安全认证
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接linux
    s.connect(hostname=hostname, username=username, password=password)
    # 执行命令
    stdin, stdout, stderr = s.exec_command('pwd')
    # 读取执行结果
    result = stdout.read()
    # 关闭linux连接
    s.close()
    # 返回执行结果
    return result


hostname=''
username=''
password=''



# 调用模块，传入liunx的ip/用户名/密码，并打印返回结果
result=con_linux(hostname=hostname, username=username, password=password)
print (result)

