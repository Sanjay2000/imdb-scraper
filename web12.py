import requests,json
from pprint import pprint 
from bs4 import BeautifulSoup
from web1 import scrape_top_list


def scrape_movie_cast(url):
		id1=(url[27:])
		# pprint(id1)
		help1=requests.get(url).text
		soup1=BeautifulSoup(help1,"html.parser")
		arti=soup1.find('div',attrs={"class":"article","id": "titleCast"})
		find=arti.find("div",class_="see-more")
		url1=find.find('a').get('href')

		hllo=("https://www.imdb.com/title/"+id1+url1)
		req=requests.get(hllo).text

		soup=BeautifulSoup(req,"html.parser")
		search=soup.find("table",class_="cast_list")
		actors=search.findAll('td',class_='')
		cast__=[]
		dict={}
		for j in actors:
			a=(j.text)
			name=(a.strip())
			imdb_id=(j.find('a').get('href')[6:15])
			# pprint(imdb_id)
			dict["name"]=name
			dict['imdb_id']=imdb_id
			cast__.append(dict.copy())
		return(cast__)

		# with open("cast.json",'w') as file:
		# 	write=json.dumps(cast__)
		# 	file.write(write)



# url_movie=scrape_top_list()
# for j in url_movie:
# 	pprint(scrape_movie_cast(j['url']))
 




