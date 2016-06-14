import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Net_neutrality")
rawdata = r.text
soup = BeautifulSoup(rawdata)

#experimented with limit
#, limit=2
print soup.find_all('p')

#https://en.wikipedia.org/wiki/Net_neutrality
#http://www.savetheinternet.com/net-neutrality-what-you-need-know-now
