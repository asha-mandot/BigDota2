import dota2api
import json
from bs4 import BeautifulSoup
import urllib2
import requests
from threading import Thread
import time
def worker(item):

	# with open("my_match_history.json", "w") as f:
		
		# match = api.get_match_details(match_id=item)
		try:
			match = []
			req = urllib2.Request("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?&key=DE5BDCD61BDD0DE4D289975A9D8F0BDA&match_id="+str(item))
			response = urllib2.urlopen(req)
			the_page = response.read()
			match = json.loads((the_page))
			match["result"]["radiant_win"] = 1
			temp= ""
			for index ,item in enumerate(match["result"]["players"]):
				print index
				# print item["account_id"]			
				if(str(item["account_id"]) == str(101678979) ):
					print "JHBJHBKBJHB" 
					temp = item
			match["result"]["players"] = temp
			match = str(match)
			match = match.replace("u","")
			match = match.replace("'" , '"')
			print match
			count = count + 1			
			# f.write(str(match)+"\n")
			# print count
		except:
			pass
		return match
	# f.close()


api = dota2api.Initialise("DE5BDCD61BDD0DE4D289975A9D8F0BDA")
account_id = '101678979'
i=0
count = 0
match =""
with open('pf_match_id/101678979') as f: 
		lines = f.readlines()
f.close()
with open("pf_match_id/101678979_match_history.json", "w") as f:
	for item in lines:	
			# print item
			match =  str(worker(str(item)) )
			# print match
			time.sleep(1)
	# print match


			f.write(str(match)+"\n")
f.close()
# threadlist = []
 
# #making threads
# while i<len(lines):
#           t = Thread(target=worker,args=(lines[i],))
#           t.start()
#           threadlist.append(t)
#           i=i+1
# for b in threadlist:
# 	b.join()