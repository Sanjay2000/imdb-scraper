from web4 import get_movie_list_details
from pprint import pprint
from web1 import scrape_top_list


url=scrape_top_list()
for i in url:
	url1=(i['url'])
pprint(url1)
detail=get_movie_list_details(url1)
pprint(detail )