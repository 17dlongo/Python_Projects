import os
import sys
import time
from datetime import datetime
sys.append('/Users/DanielLongo/Desktop/StockModule')
from Calender import MDate #makes a date (year,month,day) all in strings
from Calender import FindNofDaysBTX as MT #find time (start, finish) all strings

#Variables
stocks = {}
time = {}
mincorr = 0
length = MT(start,finish)
#Functions

def create_file(inputt):
    file = open('Correlations-'+get_datetime()+'-'+str(delay)+'')
     for item in inputt:
         file.write("%\n" % item)
    file.close()
    
def get_datetime():
    x = str(datetime.now()) # x is datetime
    x = x[:16]
    return x

def download_file(symbol):
    try:
        with open("/Users/DanielLongo/Desktop/StockModule/StockFiles/"+symbol+"", "r") as nfile:
            data = nfile.readlines()
        except FileNotFoundError:
            return None
        return data

def dpcreate(data):
    global time
    returning = {}
    x = []
    if len(data) == 0:
        return None
    for line in data:
        x.append(line.strip().split(","))
    x.pop(0)
    for countera in range(0,len(x)):
        returning[x[countera][0]] = x[countera][6] #date: close
    return returning 
        
                
    
    
