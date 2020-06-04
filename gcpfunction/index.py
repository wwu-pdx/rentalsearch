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
		address = ''
		zip = request.form['zip']
		city = request.form['city']
		state = request.form['state']

		bed = request.form['bed']
		bath = request.form['bath']
		addr =  request.form['addr']
		radius =  request.form['radius']
		#limit=10
		#offset =1

		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

		headers = {
                'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
                'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
                }
		query = f"/rentalListings?city={city}&state={state}"


		if addr and radius:
			address = f'{addr}, {city}, {state} {zip}'
			address = address.replace(",","%2C").replace(" ","%20")
			query = f"/rentalListings?radius={radius}&address={address}"
			if radius:
				query = query+ f"&radius={radius}"
				if bed:
					query =query + f"&bedrooms={bed}"
				if bath:
					query =query + f"&bathrooms={bath}"
		

		

		d = Search().search(query)
		data = sorted(d, key = lambda i: i['price']) 	
      
		
		#return redirect(url_for('index', data = {"redic":"post"}))
		return render_template('index.html', query=query, data=data)
	
	