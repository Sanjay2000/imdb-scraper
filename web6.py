from pprint import pprint 
from web5 import movie_detail_list


def analyse_movies_language():
	top_movies = movie_detail_list()[:250]
	dict={}
	list1=[]
	for j in top_movies:
		lan=(j["language"])
		for k in lan:
			if k not in list1:
				list1.append(k)
	for i in list1:
		count=0
		for x in top_movies:
			cd=(x["language"])
			for y in cd:
				if y==i:
					count+=1
				dict[i]=count
	return (dict)
pprint(analyse_movies_language())






