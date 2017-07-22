from lxml import html
import requests
from xml import etree
from lxml import html
import requests
import xml.etree.ElementTree as ET
import itertools
import csv
import time    
import glob
import os
import sys
import datetime
from datetime import timedelta
from datetime import date
import urllib.parse
from urllib import request
#from collections import OrderedDict
newTickers = []
#-456 = INVADLID DATE
def dailyReprt(stock):
    URL = 'https://finance.yahoo.com/quote/'+stock+''
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]/text()')
    change = change[0].split(" ")
    return float(change[1].strip('(').strip(')').strip('+').strip('-').strip('%'))

def str__date(day):
    day = day.split("-")
    print("DAY",day)
    print(int(day[0]),int(day[1]),int(day[2]))
    return datetime.date(int(day[0]),int(day[1]),int(day[2]))
'''
def createURL(symbol,start,end):
    print("SYMBOL",symbol)
    return "https://query1.finance.yahoo.com/v7/finance/download/"+symbol+"?period1="+str(start)+"&period2="+str(end)+"&interval=1d&events=history&crumb=U7lJqxWGiH7"
https://finance.yahoo.com/quote/AA/history?period1=1499324400&period2=1499497200&interval=1d&filter=history&frequency=1d
https://query1.finance.yahoo.com/v7/finance/download/AA?period1=1499324400&period2=1499497200&interval=1d&events=history&crumb=U7lJqxWGiH7
https://query1.finance.yahoo.com/v7/finance/download/AA?period1=1499324400&period2=1499497200&interval=1d&events=history&crumb=U7lJqxWGiH7
'''

def createURL(symbol,start,end):
    #https://www.google.com/finance/historical?q=AAPL&startdate=May+17%2C+2016&enddate=Jul+18%2C+2017&num=20&ei=0uhtWaiqM4LHU8Gko8AK&output=csv
    #https://www.google.com/finance/historical?q=AAPL&startdate=May+17%2C+2016&enddate=Jul+18%2C+2017&num=20&ei=0uhtWaiqM4LHU8Gko8AK
    #params = OrderedDict
    #params['q'] = symbol
    #params['startdate'] = start.strftime('%b %d, %Y')
    #params['enddate'] = end.strftime('%b %d, %Y')
    #params['end'] =
    params = {'q':symbol,'startdate':start.strftime('%b %d, %Y'),'enddate':end.strftime('%b %d, %Y'),'num':'20','ei':'0uhtWaiqM4LHU8Gko8AK','output':'csv'}
    params = urllib.parse.urlencode(params)
    return "https://www.google.com/finance/historical?" + params
    #"http://www.google.co.uk/finance/historical?cid=22144&startdate=Jul%2019%2C%202016&enddate=Jul%2018%2C%202017&num=200&ei=r-dtWeCPGsf2U6eJregD&start=200&output=csv"
def download(symbols,start,end):
#    start = int(time.mktime(start.timetuple()))
#    end = int(time.mktime(end.timetuple()))
    for counter in range(len(symbols)): # Downloads every stock file and sets stock ticker to a dictionary
        URL = createURL(symbols[counter],start,end)
        download_file(symbols[counter],URL)

def download_file(symbol,URL): # dowloads file as NAME.csv
    global newTickers
    file = open("STB_Files/"+symbol, "w")
    r = requests.get(URL)
    if r.status_code == 404:
        return
    if r.text == None:
        return None
    print(r.text,URL)
    newTickers += [symbol]
    try:
        file.write(r.text)
    except UnicodeEncodeError as error:
        print(symbol)
    file.close()

def report(path):
    tickers= []
    for l in open(path,'r'):
        line = l.split(',')
        tickers.append(line[0])
    tickers.pop(0)
    final0 = {}
    final1 = []
    for ticker in tickers:
        add = dailyReprt(ticker)
        final0[ticker] = add
        final1.append(add)
    avg = sum(final1)/len(final1)
    print(avg)
    return

def daily_reportII(stock,day):
  #  date = day.strftime('%m-%d-%y')
    date = day.strftime('%-d-%b-%y')
    print("HELLO WORLD")
    print(date)
    for l in open("STB_Files/" + stock, "r"):
        line = l.split(',')
        print(line)
        if line[0] == date:
            print("found")
            if line[1] == "-":
                return -456
            return (float(line[1])-float(line[4]))/float(line[1])
    return -456

def getscanNumber():
    #//*[@id="main-content"]/div[2]/div/div[2]/ul/li[1]/a[1]
    #//*[@id="main-content"]/div[2]/div/div[2]/ul/li[2]/a[1]
    #//*[@id="main-content"]/div[2]/div/div[2]/ul/li[4]/a[1]
    #//*[@id="main-content"]/div[2]/div/div[2]/ul/li[1]/a[1]
    pageContent = requests.get("https://swingtradebot.com/stock-screens/Bullish")
    tree = html.fromstring(pageContent.content)
    i = 0
    final = []
    ref = {}
    while True:
        i += 1
        add = tree.xpath('//*[@id="main-content"]/div[2]/div/div[2]/ul/li['+str(i)+']/a[1]/@href')
        if add == []:
            break
        add = add[0].strip("/events/").strip('/equities')
        code = (add[0]+add[1]).strip("-")
        ref[code] = add
        print(code)
        final += [code]

    return final

#getscanNumber()
# datetime.date = year month day

def scan_download(scan_number,date):
    #https://swingtradebot.com/events/13/equities?selected_date=07%2F18%2F2017&min_vol=250000&min_price=10&max_price=999999&adx_trend=&grade=&include_etfs=0&sector%5Bid%5D=&csv_button=as_csv
    Adate = date.strftime("%m %d %Y")
    Bdate = Adate.replace(" ","%2F")
    print(date)
    URL = "https://swingtradebot.com/events/"+str(scan_number)+"/equities?selected_date="+ Bdate +"&min_vol=250000&min_price=10&max_price=999999&adx_trend=&grade=&include_etfs=0&sector%5Bid%5D=&csv_button=as_csv"
    print("hererererere",URL)
    r = request.urlopen(URL)
    print(r.read())
    if r.status_code == 404:
        print("INVALID URL")
        return None
    if r.text == None:
        print("NO TEXT")
        return None
    with open("./"+ str(scan_number) +"/"+ date.strftime("%m_%d_%Y") +"","w") as f:
        f.write(r.text)
        f.close
    return
    '''
    file = open("./"+ str(scan_number) +"/"+ date.strftime("%m_%d_%Y") +"","w")
    try:
        file.write(r.text)
    except UnicodeEncodeError:
        print("Unicode error")
    file.close()
'''
def download_scan_dates(scan_number,start,end):
    dates = [start + timedelta(days=x) for x in range((end-start).days + 1)]
    try:
        os.makedirs("./"+str(scan_number)+"")
    except FileExistsError:
        os.system('rm'+"./"+str(scan_number)+"")
       # r = glob.glob("./"+str(scan_number)+"")
        #for l in r:
         #   os.remove(l)
    for date in dates:
        print("Hello WORLD")
        scan_download(scan_number,date)

def reportII(path,date):
    global newTickers
    newTickers = []
    tickers = []
    for l in open(path,'r'): #get the list of tickers predicted to move up (or down)
        line = l.split(',')
        tickers.append(line[0])
    start = date - timedelta(1)
    end = date + timedelta(1)
    download(tickers,start,end)
    tickers.pop(0)
    final = []
    for ticker in newTickers:
        add = daily_reportII(ticker,date + timedelta(1)) #get the acutal performance on the next day
        if add  == -456:
            print(ticker)
            continue
        final += [add]
    print(final)
    return final

def All(path):
    final = []
    files = os.listdir(path)
    files = files[1:]
    for File in files:
        print(File)
        date = File[-14:].strip(".csv")
      #  date = str__date(date)
       # date = date.replace("-","")
        date = datetime.datetime.strptime(date,"%Y-%m-%d").date()
        add = reportII(path+File,date)
        final += add
    average = (sum(final)/len(final))
    print(len(final))
    print(final)
    print(average)
    return average
download_scan_dates(11,date(2016,2,1),date(2016,2,4))
#All("./BoomerBuy/")