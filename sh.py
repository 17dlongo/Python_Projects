import json
from pprint import pprint
import urllib.request

url = 'https://www.stubhub.com/miami-heat-tickets-miami-heat-miami-american-airlines-arena-1-23-2017/event/9641076/?mbox=1&rS=6&abbyo=true&sliderpos=false&qtyq=false&qtyddab=true&dUpg=false&sort=price+asc&bla=true'

data = json.load(urllib.request.urlopen(url))
tickets = data['eventTicketListing']['eventTicket']

prices = [ticket['tc']['amount'] for ticket in tickets]
pprint(sorted(prices))
