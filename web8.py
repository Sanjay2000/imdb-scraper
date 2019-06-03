from web1 import scrape_top_list
import os,json
from pprint import pprint
from web4 import get_movie_list_details
# import time
# import random




url=scrape_top_list()
for i in url:
	u=(i['url'][-9:-1])+".json"
	if os.path.exists(u):
		# print("satyam")
		with open(u,'r+') as folder:
			# s = folder.read()
			data = json.load(folder)
			pprint(data)

	else:
	# time.sleep(random.randint(1,3))
		with open(u,'w+') as folder:
			sad=get_movie_list_details(i["url"])
			s = json.dumps(sad)
			folder.write(s)
			pprint(s)

