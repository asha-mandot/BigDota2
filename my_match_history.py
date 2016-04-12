import dota2api
api = dota2api.Initialise("DE5BDCD61BDD0DE4D289975A9D8F0BDA")


with open('pm_ids') as f: 
    lines = f.readlines()
f.close()
count = 0
with open("my_match_history", "w") as f:
	for item in lines:
		match = match = api.get_match_details(match_id=item)
		count = count + 1
		f.write(str(match)+"\n")
		print count
f.close()

