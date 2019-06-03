from web1 import scrape_top_list
import os,json
from pprint import pprint

def  analyse_movies_genre():
	url=scrape_top_list()
	dict1={}
	list1=[]
	all_data=[]
	for i in url:
		u=(i['url'][-9:-1])+".json"
		if os.path.exists(u):
			with open(u,'r+') as folder:
				data = json.load(folder)
				list1.append(data['Genres'][0])
				all_data.append(data)
	list2=[]
	for j in list1:
		if j not in list2:
			list2.append(j)
	for x in list2:
		print(x)
		count=0
		for t in all_data:
			if x in t['Genres']:
				count+=1
			dict1[x]=count
	return(dict1)
pprint( analyse_movies_genre ())
