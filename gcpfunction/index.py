from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from collections import OrderedDict


class Index(MethodView):
	def get(self):
		return render_template('index.html')

	def post(self):

		city = flask.request.form['city']
		state = flask.request.form['state']

		if city and state:

		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

		query = {"city":city,"state":state, "status"="Active"}

		headers = {
			'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
			'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
			}

		data = request("GET", url, headers=headers, params=query)
		return render_template('index.html', data=data)

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

