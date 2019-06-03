import json
from pprint import pprint



with open("total_movie.json",'r')as war:
	see=json.load(war)
def group_by_year(scrap):
	year_list=[]
	for i in scrap:
		# print(i)
		if i["year"] not in year_list:
			year_list.append(i["year"])
		# 	# print(year_list)	
	dict1={}
	for j in year_list:
		year=[]
		for x in scrap:
	# 		print (x)
			if j==x["year"]:
				year.append(x)
		dict1[j]=year
	return(dict1)
	with open("web2.json ",'w')as data:
		rap=json.dumps(dict1)



# pprint(group_by_year(see))


