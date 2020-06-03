from flask import render_template, escape
import pprint


def main(request):
#def main():
	
	request_json = request.get_json(silent=True)
	city = request_json['city']
	state = request_json['state']

	if city and state:

		url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

		querystring = {"city":city,"state":state, "status"="Active"}

		headers = {
			'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
			'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
			}

		data = request("GET", url, headers=headers, params=querystring)
	
	return render_template(f'main.html', data=data)

# if __name__ == "__main__":
# 	main()

