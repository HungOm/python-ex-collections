#!/usr/bin/env python3


import sys,os,re
import operator

user_record = dict()
err_log = dict()
with open('syslog.log') as file:
    for line in file:
        # ls = line.split()
        # print(ls)
        matchgroup = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        ms_type,msg,user = matchgroup.group(1),matchgroup.group(2),matchgroup.group(3)

        # print(ms_type,msg)
        if msg not in err_log.keys():
            err_log[msg] = 1
        else:
            err_log[msg] +=1

        if user not in user_record.keys():
            user_record[user] = {}
            user_record[user]['INFO'] = 0
            user_record[user]['ERROR'] = 0

        if ms_type =='INFO':
            
            if user not in user_record.keys():
                user_record[user] = {}
                user_record[user]['INFO'] = 0
            else:
                user_record[user]['INFO'] += 1
        elif ms_type == 'ERROR':
            
            if user not in user_record.keys():
                user_record[user] = {}
                user_record[user]['ERROR'] = 0
            else:
                user_record[user]['ERROR'] += 1
      
users = sorted(user_record.items(), key=operator.itemgetter(0))
errors = sorted(err_log.items(),key=operator.itemgetter(1),reverse=True)

errors.insert(0, ('Error', 'Count'))


with open('user_statistics.csv','w',newline = '') as user_csv:
    for key, value in users:
            user_csv.write(str(key) + ',' +
                        str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

with open('error_message.csv','w',newline='') as err_file:
    for key,value in errors:
        err_file.write(str(key)+','+ str(value)+'\n')