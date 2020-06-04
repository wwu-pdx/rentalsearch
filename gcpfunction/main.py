# import requests

# url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"

# querystring = {"city":"Hillsboro","state":"OR", "bathrooms": "1", "bedrooms":"2", "offset":"1", "limit":"5"}

# headers = {
#     'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
#     'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response)


import http.client
import json

conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
    'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
    }

conn.request("GET", "/rentalListings?radius=50&address=1900%20SW%204th%20Ave%252C%20Portland%252C%20OR%2097201", headers=headers)
#conn.request("GET", "/rentalListings?radius=50&bedrooms=2&bathrooms=1&address=1900%20SW%204th%20Ave%252C%20Portland%252C%20OR%2097201", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")


print(data)
print(type(data))

