import requests

def get_movies_by_title_year(title_query, year_query):
	address = "http://www.omdbapi.com/?s=" + title_query
	if year_query != "":
		address = address + '&?y=' + year_query
	address = address + '&apikey=82d614aa'
	response_raw = requests.get(address)
	response = response_raw.json()
	if response['Response'] == 'False':
		return {}
	else:
		qs = []
		for film in response['Search']:
			movie = {}
			movie['title'] = film['Title']
			movie['year'] = film['Year']
			qs.append(movie)
	return qs
