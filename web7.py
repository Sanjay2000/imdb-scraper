from pprint import pprint
from web5 import movie_detail_list


def analyse_movies_directors():

	top_movies = movie_detail_list()[:250]
	list1=[]
	dict={}
	for i in top_movies:
		director=(i["director"])
		for j in director:
			if j not in list1:
				list1.append(j)
	for x in list1:
		count=0
		for y in top_movies:
			dirt=(y["director"])
			for t in dirt:
				if t==x:
					count+=1
			dict[x]=count
	return dict
pprint(analyse_movies_directors())
	

