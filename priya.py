import json
from pprint import pprint

with open('p.json','r') as data_file:    
    data = json.load(data_file)

print type(data['result']['players'])

