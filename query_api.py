import dota2api
from bs4 import BeautifulSoup
import urllib2
import json
# this fetches reponse from the api
def fetch(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
	return the_page



#this process the collectiong players personal matchids page by page by forming the url automatically
remaining_results = -1
all_matchid = []
checker = 1
url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA"	
while(remaining_results != 0):
	
	soup = BeautifulSoup(fetch(url), "html.parser")

	if(checker == 1):
		remaining_results = soup.find("results_remaining")
		print remaining_results
		matches = soup.find('matches')
	
		match = matches.find_all('match')
		checker = checker + 1
		count =0
		for item in match:
			matchid = item.find('match_id')
			count = count + 1
			# print matchid.text
			all_matchid.append(matchid.text)
			# print count
	else:
		matches = []
		soup = str(soup)
		matches = json.loads(soup)
		remaining_results = matches["result"]["results_remaining"]

		match = matches["result"]["matches"]
		for item in match:
			# matchid = item.find('match_id')
			count = count + 1
			# print item["match_id"]
			all_matchid.append(item["match_id"])
			# print count
	# count =0
	
	start_at_match_id = all_matchid[len(all_matchid) - 1]
	# print remaining_results
	url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?start_at_match_id="+str(start_at_match_id)+"&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA"

	# print url
all_matchid = list(set(all_matchid))
count =0
for item in all_matchid:
	print item 
	count = count + 1
	print count 