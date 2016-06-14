import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Net_neutrality")
rawdata = r.text
soup = BeautifulSoup(rawdata)

#experimented with limit
#, limit=2
print soup.find_all('p')

#https://en.wikipedia.org/wiki/Net_neutrality

#can alternatively write to a file
