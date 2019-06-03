import json
from pprint import pprint 
from web2 import group_by_year
with open("total_movie.json",'r')as file:
	data=json.load(file)
	# print (data)

movies_by_year = group_by_year(data)

def group_dicade(raper):
	year_list=[]
	for i in raper:
		if i["year"] not in year_list:
			year_list.append(i["year"])
	max1 =(max(year_list))
	min1=(min(year_list))
	while True:
		if min1%10!=0:
			min1-=1
		elif max1%10!=0:
			max1+=1
		else:	
			break
	lst=[]
	dict1={}
	for x in range(min1,max1+1,10):
		lst.append(x)
	for a in lst:
		list1=[]
		for i in movies_by_year:
			# print (i)
			if a<i and a+10>i:
				list1.append(movies_by_year[i][0])
		dict1[a]=list1
	return (dict1)

pprint(group_dicade(data))

