import dota2api
from bs4 import BeautifulSoup
import urllib2
import json

def fetch(url):
	try:
		print "sdfsd"
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		the_page = response.read()
		soup = BeautifulSoup(the_page, "html.parser")

		if (soup.find("status").text == "15"):
			print "vachindi"
			return None
		else:
			print "raledhu"
			return soup
	except:
		pass

def process(ac_id):
	remaining_results = -1
	all_matchid = []
	# checker = 1
	soup = str(-1)
	url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA&account_id="+str(ac_id)	
	while(remaining_results != "0" and soup != None):

		soup = fetch(url)		
		print soup
		if(soup != None):
			remaining_results = soup.find("results_remaining").text
			matches = soup.find('matches')
		
			match  = matches.find_all('match')
			# checker = checker + 1
			count =0
			for item in match:
				matchid = item.find('match_id')
				count = count + 1
				# print matchid.text
				all_matchid.append(matchid.text)

			start_at_match_id = all_matchid[len(all_matchid) - 1]
			remaining_results = soup.find("results_remaining").text
			print remaining_results
			url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&start_at_match_id="+str(start_at_match_id)+"&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA&account_id="+str(ac_id)

	all_matchid = list(set(all_matchid))
	count =0
	f= open(str(ac_id), "w")
	for item in all_matchid:
		# print item 
		count = count + 1
		f.write(str(item)+ "\n")
		# print count 
	f.close()


with open('pf_ac_ids') as f:
    lines = f.readlines()
f.close()

for ac_id in lines:
	print ac_id
	process(ac_id)    