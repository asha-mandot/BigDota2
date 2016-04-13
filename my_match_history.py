import dota2api
import json
from bs4 import BeautifulSoup
import urllib2

api = dota2api.Initialise("DE5BDCD61BDD0DE4D289975A9D8F0BDA")
account_id = '218208737'

with open('pm_ids') as f: 
    lines = f.readlines()
f.close()
count = 0
with open("my_match_history", "w") as f:
	# for item in lines:
		# match = api.get_match_details(match_id=item)
		match = []
		req = urllib2.Request("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA&match_id=2259422420")
		response = urllib2.urlopen(req)
		the_page = response.read()
		match = json.loads((the_page))
		# print match
		for index ,item in enumerate(match["result"]["players"]):
			print index
			print item["account_id"]
			
			if(str(item["account_id"]) != str(218208737) ):
				# match["result"]["players"].remove(item)
				match["result"]["players"].pop(index)
				# print item["account_id"]
			count = count + 1
		f.write(str(match)+"\n")
		print count
f.close()

