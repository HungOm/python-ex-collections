#!/usr/bin/python3
__author__ = "Om"
__EMAIL__ = 'hungomoct19@outlook.com'

import paramiko
import time

Channel = paramiko.SSHClient()
Channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
Channel.connect(hostname="172.27.158.218", look_for_keys=False,allow_agent=False)
shell = Channel.invoke_shell()


shell.send("enable\n")
shell.send("access123\n")
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
shell.send("show arp \n")
time.sleep(2)
print(shell.recv(5000))
Channel.close()