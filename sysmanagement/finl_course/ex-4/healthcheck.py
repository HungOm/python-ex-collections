#!/usr/bin/env python3
import psutil
import socket
import report_email
import os

def check_localhost():
    return socket.gethostbyname('localhost')!='127.0.0.1'

def check_cpu():
    return psutil.cpu_percent()>80

def check_available_memory():
    THRESHOLD = 500 * 1024 * 1024
    mem = psutil.virtual_memory()
    return mem.available<THRESHOLD

def check_disk():
    obj_Disk = psutil.disk_usage('/')
    avaible_percentage = round((obj_Disk.free /obj_Disk.total*100),2)
    return avaible_percentage<20

# setswitchinterval

# print(check_cpu())
# print(check_available_memory())
# print(check_disk()) 

def send_report(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = subject
    body = "Please check your system and resolve the issue as soon as possible.\n"
    message = report_email.generate(sender, receiver, subject, body)
    report_email.send(message)
    

if __name__ =="__main__":
        
    if check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        send_report(subject)
        print("Sent: {}".format(subject))
    if check_available_memory():
        subject = "Error - Available memory is less than 500MB"
        send_report(subject)
        print("Sent: {}".format(subject))
        
    if check_cpu():
        subject = "Error - CPU usage is over 80%"
        send_report(subject)
        print("Sent: {}".format(subject))
        
    if check_disk():
        subject="Error - Available disk space is less than 20%"
        send_report(subject)
        print("Sent: {}".format(subject))