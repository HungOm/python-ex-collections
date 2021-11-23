#!/usr/bin/env python3
import csv
import datetime
import requests
FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)
def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines
def get_same_or_newer(data,start_date):
    """Returns the employees that started on the given date, or the closest one."""
    reader = csv.reader(data[1:])
    data1 = sorted(reader, key = lambda row: datetime.datetime.strptime(row[3], '%Y-%m-%d'))
    # # We want all employees that started at the same date or the closest newer
    # # date. To calculate that, we go through all the data and find the
    # # employees that started on the smallest date that's equal or bigger than
    # # the given start date.
    today = datetime.datetime.today()
    min_date =datetime.datetime.strftime(today,'%Y-%m-%d')
    start_date = start_date.strftime('%Y-%m-%d')

    min_date_employees = {}
    for data in data1:
        # if data[3] < start_date:
        #     continue
  
        # if data[3] < min_date:
        #     min_date = data[3]
        #     min_date_employees[min_date] = []
        #     continue
        name = "{} {}".format(data[0],data[1])
        if data[3] in min_date_employees:
            min_date_employees[data[3]].append(name)
            continue
        min_date_employees[data[3]]= [name]
    if min_date not in min_date_employees:
        min_date_employees[min_date]=[]
            
    return min_date_employees
def list_newer(start_date):
    data = get_file_lines(FILE_URL)
    employees = get_same_or_newer(data,start_date)
    for date in employees:
         print("Started on {}: {}".format(date,employees[date]))
def main():
    start_date = get_start_date()
    list_newer(start_date)
if __name__ == "__main__":
    main()