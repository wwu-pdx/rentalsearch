from flask import render_template
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
import pprint

def main(request):
	
	address = '1600 Pennsylvania Ave NW, Washington, DC'
	zipcode = '20006'
	zillow_data = ZillowWrapper('X1-ZWz176n7hv7nd7_7dhgw')
	deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
	result = GetDeepSearchResults(deep_search_response)
	#print(result.zillow_id)
	#pp = pprint.PrettyPrinter(indent=2)
	#pp.pprint (result.zillow_id)
	
	return render_template(f'main.html', result=result)

