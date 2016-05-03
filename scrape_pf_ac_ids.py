import urllib
from bs4 import BeautifulSoup
import re
from threading import Thread
 
#yrl to scrape professional account players
url = "http://dotamax.com/player/" 


#scrapes the html content here
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# print soup


#finds the table with rewuired table and writes them in to a file
rows = soup.find_all('tr')
f = open("pf_ac_ids" , "w")
for item in rows:
     span = item.find("span")
     print span.text
     f.write(span.text + "\n")
f.close()
