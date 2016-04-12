import urllib
from bs4 import BeautifulSoup
import re
from threading import Thread
 
#List of yelp urls to scrape

url = "http://dotamax.com/player/" 


 
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# print soup


# table = soup.find('table')
# print table
rows = soup.find_all('tr')
f = open("pf_ac_ids" , "w")
for item in rows:
     span = item.find("span")
     print span.text
     f.write(span.text + "\n")
f.close()
