import requests
from bs4 import BeautifulSoup
from pprint import pprint
import random
from web12 import scrape_movie_cast


def get_movie_list_details(link):


		
	url=requests.get(link)
	soup=BeautifulSoup(url.text,"html.parser")

	#####........Name......
	name=soup.find("h1").text
	name=(name[:-7].replace(u'\xa0', u''))
	#.........dicrctor.......

	dir_list=[]
	director = soup.find("div",class_="credit_summary_item")
	# print (director)
	rape = director.findAll('a')
	# print (dir1)
	for x in rape:
		dir_list.append(x.text)
	#........Bio........#

	bio = soup.find("div",class_="summary_text").text


	time=soup.find("div",class_="title_block")
	runtime=time.find("time").text.strip()
	tm=runtime.split()
	if len(tm) == 1:
		hours = int(tm[0][0])*60
	else:
		hours = int(tm[0][0])*60 + int(tm[1][:-3])
	# print (str(hours) + ' minutes')

	# ..........image url.....

	image1 = soup.find('div', class_ = 'poster')
	photo = image1.find('a').img['src']

	###country#####
	###..language....
	#...runtime...

	country = soup.find("div", attrs= {"class": "article", "id": "titleDetails"})
	desh=country.findAll("div",class_="txt-block")
	language_list=[]
	wild=[]

	for i in desh:
		h4 = i.find('h4')
		if h4:
			if (h4.text == 'Language:'):
				language = i.findAll('a')
				for j in language:
					language_list.append(j.text)
			if (h4.text == 'Country:'):
				country_name = i.find('a')
				wild.append(country_name.text)
	# pprint(wild)
	# pprint(language_list)			
			# break

	##geners#######

	geners=soup.find("div",attrs={"class":"article","id": "titleStoryLine"})
	drama=geners.findAll("div",class_="see-more inline canwrap")
	list1=[]
	for j in drama:
		h4 =j.find("h4")
		if (h4.text=="Genres:"):
			gn=j.findAll("a")
			for k in gn:
				list1.append(k.text)
	# print (list1)


	dic={'name': name,
		'director': dir_list,
		'language': language_list,
		'bio': bio,
		'runtime': str(hours) + ' minutes', 	
		'poster_image_url': photo,
		'Genres': list1,
		'country': wild,
		'cast':scrape_movie_cast( )
		}

	return (dic)
# pprint (get_movie_list_details("https://www.imdb.com/title/tt0066763/"))










