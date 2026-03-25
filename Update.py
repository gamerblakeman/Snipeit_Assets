import json
import requests
import time
serverURI = "http://localhost:8000"
from Veriables import key

requestcounter = 0
def create(server, token, payload):
        global requestcounter
        """Create new maintenances data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        uri = '/api/v1/maintenances'
        server = server + uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(server, headers=headers, data=payload)
        requestcounter += 1

        #b'{"status":"error","messages":{"start_date":["The start date must be a valid date in YYYY-MM-DD format"],"completion_date":["The completion date field must match the format Y-m-d.","The completion date field must be a date after or equal to start date."]},"payload":null}'
        if(results.json().get("status") == "error"):
            print("Error creating maintenance: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

def getDetailsByTag(server, token, AssetTag):
        global requestcounter
        """Get asset details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetTAG {string} -- Asset TAG             
        
        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        uri = '/api/v1/hardware/bytag/{0}'.format(str(AssetTag))
        server = server + uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(server, headers=headers)
        requestcounter += 1
        if(requestcounter > 980):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        if(results.json().get("status") == "error"):
            print("Error creating maintenance: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return results.content

def auditAsse123t(server, token, assetTag):
        global requestcounter
        """Audit an asset
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            assetTag {string} -- asset tag to be audited (default: {None})
            locationID {[type]} -- location ID to be audited (default: {None})
        """
        uri = '/api/v1/hardware/audit'
        payload  = {'asset_tag':str(assetTag)}
        server = server + uri
        headers = {"Accept": "application/json", "accept": "application/json",'content-type': 'application/json','Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        print(payload)
        print(server)
        print(headers)
        # use json= so content-type matches and body is valid JSON
        results = requests.post(server, headers=headers, json=payload)
        requestcounter += 1
        if(results.json().get("status") == "error"):
            print("Error creating maintenance: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        try:
            return json.dumps(results.json(),indent=4, separators=(',', ':'))
        except json.JSONDecodeError:
            return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

def auditAsset(server, token, assetTag=None, locationID=None):
        global requestcounter
        """Audit an asset
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            assetTag {string} -- asset tag to be audited (default: {None})
            locationID {[type]} -- location ID to be audited (default: {None})
        """
        uri = '/api/v1/hardware/audit'
        payload  = {'asset_tag':assetTag, 'location_id':locationID}
        server = server + uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        # send JSON payload, otherwise requests will form‑encode it which the API rejects
        results = requests.post(server, headers=headers, json=payload)
        requestcounter += 1
        if(results.json().get("status") == "error"):
            print("Error creating maintenance: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

#
#curl --request POST \
#     --url http://localhost:8000/api/v1/hardware/audit \
#     --header 'Accept: application/json' \
#     --header 'Authorization: Bearer KEY' \
#     --header 'accept: application/json' \
#     --header 'content-type: application/json' \
#     --data '{"asset_tag":"4063"}'

def Update(ID, dataIn, Date):
    global requestcounter
    print("Request Counter: " + str(requestcounter))
    data = getDetailsByTag(serverURI, key, ID)
    jsonData = json.loads(data)
    __id = jsonData["id"]
    jsonData = {
    "asset_maintenance_type": "PAT Test",
    "start_date": Date,
    "completion_date": Date,
    "notes": dataIn,
    "name": "PAT Test - " + ID,
    "asset_id": __id
    }
    print("Request Counter: " + str(requestcounter))
    create(serverURI, key, json.dumps(jsonData))
    print("Request Counter: " + str(requestcounter))
    #auditAsset(serverURI, key, str(ID))
