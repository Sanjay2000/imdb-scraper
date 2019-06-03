
from pprint import pprint 
from web1 import scrape_top_list
from web4 import get_movie_list_details

def movie_detail_list():
	list1=[]
	top_movies = scrape_top_list()
	for i in top_movies:
		link=(i["url"])
		data=get_movie_list_details(link)
		list1.append(data)
	return (list1)
pprint(movie_detail_list())


