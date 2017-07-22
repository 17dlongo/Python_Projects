from lxml import html
import requests
from xml import etree
from lxml import html
import requests
import xml.etree.ElementTree as ET
import itertools
import csv
import time
#//*[@id="lookup-page"]/section/div/div/div[1]/div/div[3]/span[1]/a

#URL = "https://finance.yahoo.com/lookup?s=abc"
#page = requests.get(URL)
#tree = html.fromstring(page.content) //*[@id="mw-content-text"]/table[1]/tbody/tr[2]/td[2]/a[1]
#text = tree.xpath('//*[@id="lookup-page"]/section/div/div/div[1]/div/div[10]/span[1]/a/text()')
#print(text)
'''
//*[@id="mw-content-text"]/table[1]/tbody/tr[2]/td[2]/a[1]
//*[@id="mw-content-text"]/table[1]/tbody/tr[4]/td[2]/a[1]
//*[@id="mw-content-text"]/table[1]/tbody/tr[6]/td[2]/a[1]

'''
'''
//*[@id="tab2"]/table[1]/tbody/tr[2]/td/a[1]

//*[@id="tab2"]/table[6]/tbody/tr[1]/td[2]/a
//*[@id="tab2"]/table[6]/tbody/tr[1]/td[3]/a

//*[@id="tab2"]/table[6]/tbody/tr[2]/td[2]/a

'''

def scrape():
    URL = 'https://www.ustanorcal.com/playermatches.asp?id=158918&a=T&l=500009117&seasonid=2017#match'
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    text = tree.xpath('//*[@id="tab2"]/table[6]/tbody/tr[1]/td/a/text()')
    print('text',text)
#scrape()

def get_tickers(letters):
    tickers = []
    rep = 0
    request = 0
    for i in range(len(letters)):
        letter = letters[i]
        b = -20 #so loop will start at 0
        while True:
            b += 20
            URL  = "https://finance.yahoo.com/lookup/stocks?s="+letter+"&t=A&m=ALL&b="+str(b)+""
            print(request,URL)
            request += 1
            if request % 2000 == 0:
                print('sleeping')
                time.sleep(3600)
                print('awake')
            try:
                page = requests.get(URL)
            except:
                print('ERROR')
            tree = html.fromstring(page.content)
            add = []
            for i in range(22): # because there are 21 (indexed at 2) tickers per page
                text = tree.xpath('//*[@id="lookup-page"]/section/div/div/div[1]/div/div['+str(i)+']/span[1]/a/text()')
 #               print(text)
                if add in tickers:
                    rep += 1
                    continue
                add += text
            if len(add) == 0:
                break
 #           print(add)
            tickers += add
    print('repeates',rep)
    with open("tickerss.txt","w") as file:
        for item in tickers:
            file.write("%s\n"%item)
    return 

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 3)]
get_tickers(alphabets)

print('All Done :)')        
'''
page = requests.get('https://finance.yahoo.com/lookup?s=a')
tree = html.fromstring(page.content)
#print(page.content)
text = tree.xpath('//p[@type="text"]/text()')
print(text)

from lxml import html
import requests

page = requests.get('https://finance.yahoo.com/lookup?s=atny')
tree = html.fromstring(page.content)
print(type(page.content))
print(tree)
#print(page.content)
#text = tree.xpath('//p[@class title =""]/text()')
#print(text)
URL = "https://finance.yahoo.com/lookup?s=abc"
page = requests.get(URL)
root = ET.fromstring(page.text)
for channel in root:
    for item in channel.findall:
        symbol = item.find("title").text
        print(symbol)
'''
