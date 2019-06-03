from web1 import scrape_top_list
import os,json
from pprint import pprint
from web4 import get_movie_list_details
# import time
# import random




url=scrape_top_list()
for i in url:
	u=(i['url'][-9:-1])+".json"
	with open(u,'r+') as folder:
		data = json.load(folder)
		dic={}
		for j in data['cast']:
			if j['name'] not in data:
				dic[j['name']]=1
			else:
				dic[j['name']]+=1
		pprint(dic)
