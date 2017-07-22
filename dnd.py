from base64 import b64encode
from urllib.request import Request, urlopen
import urllib
import json
import requests

app_token = "fCphd4DQtId2jUuYqGToWhnxf0ga"
consumer_key = "3LRfESibcq2K5FC8OEM8FKcd7Lga"
consumer_secret = "Iu2TyDMGRMyE0Ct8CikxZEvyUMca"
key_secret = consumer_key+":"+consumer_secret
key_secret = b64encode(key_secret.encode())
req  = Request("https://api.stubhubsandbox.com/login")
url = 'https://api.stubhub.com/login'
key_secret = key_secret.decode("utf-8")
req.add_header('Authorization','Basic '+str(key_secret))
body = {'grant_type':'password','username':'danieldominiclongo@gmail.com','password':'Daniel1942','scope':'PRODUCTION'}
headers = {'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic '+str(key_secret)}
body = urllib.parse.urlencode(body)
body = body.encode('utf-8')
response = requests.post(url,data=body,headers=headers)
print(response.json())
#print(dir(response))
print(response.headers)

