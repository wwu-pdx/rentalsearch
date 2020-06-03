from collections import OrderedDict
import requests
import http.client

class Search():

    def __init__(self):
        pass

    def search(self, query):
        print(f'search {query}')
            
        if len(query) >0:
            print(f"here")
            
            conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")
                

            headers = {
                'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
                'x-rapidapi-key': "e22db4aecdmshd349a536e367dffp141a7djsn78c642d73125"
                }

            conn.request("GET", query, headers=headers)

            res = conn.getresponse()
            data = res.read().decode("utf-8")
            print(type(data))
            #data = [{"item1":1},{"item2":1}]
                
        
            return data