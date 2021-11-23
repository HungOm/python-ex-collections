#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime
from run import serialize_file_content
# import pdb
import os


DIR = 'supplier-data/descriptions'

# def extract_dict(obj):
#     wanted_keys =["name","weight"]
#     dic = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
#     filtered = dic(obj,wanted_keys)
#     # for key, val in ls.items():
#     #     new_list.append([key,val])
#     return filtered

def format_dic_paragraph(dic):
    return "name: {} <br/> weight: {} <br/><br/> \n".format(dic["name"],dic['weight'])
    

def filter_data(listOfobj):  
    ls = list(map(format_dic_paragraph,listOfobj))
    return ls
def format_title(strr):
    currentDay = datetime.now().day
    currentMonth = datetime.now().strftime('%B')
    currentYear = datetime.now().strftime("%Y")
    return " {} {} {}, {}".format(strr,currentMonth,currentDay,currentYear)




def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1,20)

    return report.build([report_title, empty_line, report_info, empty_line])


if __name__ =="__main__":
    listOfObject = serialize_file_content(DIR)
    data = ''.join(filter_data(listOfObject))
    path = os.getcwd()
    generate_report(path+"/processed.pdf", format_title("Processed Update on"),data)

  