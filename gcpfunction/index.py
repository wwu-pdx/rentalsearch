from flask import redirect, request, url_for, render_template
from flask.views import MethodView

from collections import OrderedDict
import requests
from search import Search

class Index(MethodView):

	# def get(self):
	# 	print("get")
	# 	return render_template('index.html')


	def get(self):
		
		if request.args.get('data'):
			data = request.args.get('data')
			return render_template('index.html', data=data)
		else:	
			return render_template('index.html')
	
	

	def post(self):

		print("post")

		city = request.form['city']
		state = request.form['state']
		bed = request.form['bed']
		bath = request.form['bath']
		limit=10
		offset =1

		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

		headers = {
                'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
                'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
                }
		
		if city and state:
			query = f"/rentalListings?city={city}&state={state}"
			#query = {"city":city,"state":state,  "limit": 2, "offset":1}

			data = Search().search(query)
			

		#print(data)
		#return redirect(url_for('index', data = {"redic":"post"}))
		return render_template('index.html', query=query, data=data)
	
	# def search(query):
	# 	print(query)
	# 	data={}
	# 	if len(query) >0:
	# 		print(query)
	# 		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

	# 		headers = {
	# 				'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
	# 				'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
	# 				}

	# 		data = requests.request("GET", url, headers=headers, params=query)
	# 	print(data)
	# 	# return data

# def main(request):
# def main():
	
# 	request_json = request.get_json(silent=True)
# 	city = request_json['city']
# 	state = request_json['state']

# 	if city and state:

# 		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

# 		querystring = {"city":city,"state":state, "status"="Active"}

# 		headers = {
# 			'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
# 			'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
# 			}

# 		data = request("GET", url, headers=headers, params=querystring)
	
# 	return render_template(f'main.html', data=data)

# if __name__ == "__main__":
# 	main()

