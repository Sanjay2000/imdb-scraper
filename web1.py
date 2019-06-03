
#     webscraping__________task- [:-1]


import requests,json
from pprint import pprint 
from bs4 import BeautifulSoup
import time,random


def scrape_top_list():

	url="https://www.imdb.com/india/top-rated-indian-movies/"
	page=requests.get(url).text
	soup =BeautifulSoup(page,"html.parser")
	need=soup.find("tbody",class_="lister-list")
	trs=need.find_all("tr")
	rank = 0
	a=[]
	for tr in trs:
		dict1={}
		rank+=1
		name= tr.find("td",class_="titleColumn").a.get_text()
		year = tr.find("td",class_="titleColumn").span.get_text()
		rating = tr.find("td",class_="ratingColumn").strong.get_text()
		url = tr.find("td",class_="titleColumn").a["href"]
		dict1["name"]=name
		dict1["year"]=int(year[1:5])
		dict1["rank"]=rank
		dict1["url"]='https://www.imdb.com'+url[:17]
		# pprint(dict1)
		a.append(dict1)
	with open("total_movie.json",'w') as dar:
		war=json.dumps(a)
		dar.write(war)
	return (a)
# pprint(scrape_top_list())



