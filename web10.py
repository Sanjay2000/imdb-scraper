# from web1 import scrape_top_list
# import os,json
# from pprint import pprint
# url=scrape_top_list()
# dirt=[]
# language=[]
# all_data=[]
# dite={}
# for i in url:
# 	u=(i['url'][-9:-1])+".json"
# 	if os.path.exists(u):
# 		with open(u,'r+') as folder:
# 			data = json.load(folder)
# 			dirt.append((data["director"]))
# 			language.append((data["language"])[0])
# 			all_data.append(data)

# # list1=[]
# # for j in dirt:
# # 	if j not in list1:
# # 		list1.append(j)
# # pprint(list1)
# # list2=[]
# # for x in language:
# # 	if x not in list2:
# # 		list2.append(x)
# # pprint(list2)

# # for y in list1:
# # 	dict1={}
# # 	for r in list2:
# # 		count=0
# # 		for t in all_data:
# # 			if y in t["director"]:
# # 				if r in t["language"]:
# # 					count+=1
# # 		if count>0:
# # 			dict1[r]=count
# # 	dite[y]=dict1
# # pprint (dite) 


