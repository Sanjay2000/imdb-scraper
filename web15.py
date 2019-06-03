from pprint import pprint
from web1 import scrape_top_list
import json


url=scrape_top_list()
dic={}
data = []
for i in url:
	bigDic = {}
	u=(i['url'][-9:-1])+".json"
	with open(u,'r+') as folder:
		temp = json.load(folder)
	data.append(temp)
for movie in data:
	for actor in movie['cast']:
		bigDic[actor["imdb_id"]] = {"num_movies" : 0, "name" : actor['name']}
for movie in data:
	for actor in movie['cast']:
		bigDic[actor['imdb_id']]['num_movies'] += 1
for movie in data:
	for actor in movie['cast']:
		if bigDic[actor['imdb_id']]['num_movies'] == 1: 
			del bigDic[actor['imdb_id']] 
pprint(bigDic)












