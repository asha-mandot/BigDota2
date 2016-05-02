import dota2api
import json
api = dota2api.Initialise("DE5BDCD61BDD0DE4D289975A9D8F0BDA")

heroes = api.get_heroes()
items = api.get_game_items()
heroes = str(heroes)
items = str(items)
items= json.loads((str(items))


heroes = heroes.replace("u","")
heroes = heroes.replace("'",'"')

items = items.replace("u","")
items = items.replace("'",'"')
# print heroes
print "*******************"
# print items



with open("hero_summary.json", "w") as f:
	f.write(heroes)
f.close()

with open("item_summmary.json", "w") as f:
	f.write(str(items))
f.close()