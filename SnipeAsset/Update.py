import json
import requests
import time
requestcounter = 0
MaxCounter = 1980

def _fetch_paginated(server, token, path, limit=500):
    """Helper to fetch all pages from SnipeIT endpoints with robust pagination.

    Tries offset-based pagination first (preferred for SnipeIT), then page-based fallback if duplicates or no progress.
    """
    def _get_rows(uri):
        url = server + uri
        headers = {'Authorization': f'Bearer {token}', 'accept': 'application/json', 'Content-Type': 'application/json'}
        resp = requests.get(url, headers=headers)
        global requestcounter
        requestcounter += 1
        if requestcounter > MaxCounter:
            print(f"Request Counter: {requestcounter} - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        return resp.json()

    all_rows = []
    seen_ids = set()
    offset = 0
    total = None

    # First pass: offset mode
    while True:
        uri = f"{path}?limit={limit}&offset={offset}"
        data = _get_rows(uri)
        page_rows = data.get('rows', [])

        if total is None:
            total = data.get('total', len(page_rows))

        duplicates = sum(1 for r in page_rows if r.get('id') in seen_ids)
        if duplicates > 0 and offset > 0:
            # offset mode seems to repeat data; fallback to page mode
            break

        for row in page_rows:
            rid = row.get('id')
            if rid not in seen_ids:
                seen_ids.add(rid)
                all_rows.append(row)

        print(f"[DEBUG] {path} offset={offset} rows_this_page={len(page_rows)} duplicates={duplicates} total={total} combined={len(all_rows)}")

        if not page_rows or (total and len(all_rows) >= total):
            return {'rows': all_rows, 'total': total or len(all_rows)}

        offset += limit

    # Fallback: page mode
    all_rows = []
    seen_ids.clear()
    page = 1
    while True:
        uri = f"{path}?limit={limit}&page={page}"
        data = _get_rows(uri)
        page_rows = data.get('rows', [])

        if total is None:
            total = data.get('total', len(page_rows))

        for row in page_rows:
            rid = row.get('id')
            if rid not in seen_ids:
                seen_ids.add(rid)
                all_rows.append(row)

        print(f"[DEBUG] {path} page={page} rows_this_page={len(page_rows)} total={total} combined={len(all_rows)}")

        if not page_rows or (total and len(all_rows) >= total):
            break

        page += 1

    return {'rows': all_rows, 'total': total or len(all_rows)}


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
        #print(results)
        #print("Error Below")
        #b'{"status":"error","messages":{"start_date":["The start date must be a valid date in YYYY-MM-DD format"],"completion_date":["The completion date field must match the format Y-m-d.","The completion date field must be a date after or equal to start date."]},"payload":null}'
        if(results.json().get("status") == "error"):
            #print("Error creating maintenance: " + str(results.json().get("messages")))
            #print(results)
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

def getDetailsByTagOLD(server, token, AssetTag):
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
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        #print(results.content)
        #print("Error Below")
        if(results.json().get("status") == "error"):
            print("Recived Error: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return results

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
        headers = {'Authorization': 'Bearer {0}'.format(token), 'accept': 'application/json', 'Content-Type': 'application/json'}
        results = requests.get(server, headers=headers)
        requestcounter += 1
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        #print(results.content)
        #print("Error Below")
        if(results.json().get("status") == "error"):
            print("Recived Error: " + str(results.json().get("messages")))
            #raise Exception("Error creating maintenance: " + str(results.json().get("messages")))

        return results

def createModel(server, token, id, Name):
        global requestcounter
        payload = {
            "name": Name,
            "model_number": id,
            "category_id": 2,
        }
        """Create new model data.
        
        Create new model data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        uri = '/api/v1/models'
        server = server + uri
        #print(server)
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token), 'accept': 'application/json'}
        results = postRequest(server, headers, payload)
        #print(results.content)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

def updateModel(server, token, id, Model, Name, catID):
        global requestcounter
        payload = {
            "name": Name,
            "model_number": str(Model),
            "category_id": catID
        }
        """Update model data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        uri = '/api/v1/models/'+str(id)
        server = server + uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.put(server, headers=headers, data=json.dumps(payload))
        requestcounter += 1
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        return json.dumps(results.json(),indent=4, separators=(',', ':'))
        
def pullModel(server, token):
        """Pull model data (all pages)."""
        response = _fetch_paginated(server, token, '/api/v1/models', limit=1000)
        return json.dumps(response, indent=4, separators=(',', ':'))

def pullLocations(server, token):
        """Pull location data (all pages)."""
        response = _fetch_paginated(server, token, '/api/v1/locations', limit=1000)
        return json.dumps(response, indent=4, separators=(',', ':'))

def pullAssetLarge(server, token):
        """Pull asset data (all pages)."""
        # SnipeIT uses 500/1000 page-size ceilings for hardware; avoid offset gaps by using 500.
        response = _fetch_paginated(server, token, '/api/v1/hardware', limit=500)
        return json.dumps(response, indent=4, separators=(',', ':'))


def createAsset(server, token, Divice, ID):
        
        payload = {
            "archived": False,
            "warranty_months": None,
            "depreciate": False,
            "supplier_id": None,
            "requestable": False,
            "rtd_location_id": None,
            "location_id": Divice["location_ID"],
            "asset_tag": ID,
            "status_id": 2,
            "model_id": Divice["itemtype_ID"],
            "name": ID,
            "last_audit_date": Divice["date"],
            "next_audit_date": Divice["nextdate"],
            "_snipeit_pattest_result_2" : Divice["OverallResult"]
        }
        """Create new asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Asset data
        
        Returns:
            [string] -- Server response in JSON formatted
        """
        uri = '/api/v1/hardware'
        server = server + uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token), 'accept': 'application/json'}
        results = postRequest(server, headers=headers, json=payload)
        #print(results)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))


def deleteAsset(server, token, id):
        """Delete an asset
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            id {string} -- Asset ID to be deleted
        """
        uri = '/api/v1/hardware/'+str(id)
        server = server + uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(server, headers=headers)
        global requestcounter
        requestcounter += 1
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

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
        #print(payload)
        #print(server)
        #print(headers)
        # use json= so content-type matches and body is valid JSON
        results = postRequest(server, headers, payload)
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
        results = postRequest(server, headers, payload)
        if(results.json().get("status") == "error"):
            print("Error creating maintenance: " + str(results.json().get("messages")))
            raise Exception("Error creating maintenance: " + str(results.json().get("messages")))
        return json.dumps(results.json(),indent=4, separators=(',', ':'))
def postRequest(server, headers, json):
    global requestcounter
    requestcounter += 1
    if(requestcounter > MaxCounter):
        print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
        time.sleep(60)
        requestcounter = 0
    results = requests.post(server, headers=headers, json=json)
    return results
#
#curl --request POST \
#     --url http://localhost:8000/api/v1/hardware/audit \
#     --header 'Accept: application/json' \
#     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTkwYmM2YjRmZGNjMjc3NzY4OWZkNTBjZDhiZGY5Zjk2MDA0YmIxZjI2Y2QxMDNkZTlkMjk2ZDlkNjA5ZmQ5ZjE3ZGM2NzAyMjQ0MjI4MzgiLCJpYXQiOjE3NzIyOTc3NDguNTc0MjM3LCJuYmYiOjE3NzIyOTc3NDguNTc0MjM4LCJleHAiOjMwMzQ2MDE3NDguNTcxMTAyLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.ap0_isUdId3dH8qGGVMrXQYFQUNjOqe_mjEK_Uq7QGtFZrkFXgeeJaTEOzkG9hU116vl_6vm_PBagA60KTNk_4IyZ0eLxk2PLpz8iRuy6M4Xy72RmoETUcluVVN-SKCK3cViNMuZ5Ldsm6ytV6k-PcOt-IuO6NnmirLbFOjYKszqR5I6wz2vQtLjvgk50vbVyNTUI0AMZ6CgffB_GV_LmZ0-oCeBMezXxS5ooBkHX5a7bQnZJMgtmdNyX9cqWjDvTib5IORRcgPmEWYw3WF39ac45fuax6WF77br7d2rfY06jJgwRe1M0heBVIIlq8qaflGWBTaDvWF2IL15OX6aDksm_6noTm0saZIx1-8AOEkNmCTF4Y70V2CN8gNhgg8c5ivFGQyXc99eGMa6Lz1LO0NXLVqnU1p0y5n6uxm0uSnZxNed9dpLGaEbuN2PcY2Oxwk8gXRLExH85nbV5-7_H-u8Map2yp0ZOCfdAqX4G3LOxP4XUAVtzZOjVSTWPe_cpMX7bk6AqmF4dFh0qk-QVeV6wbukMp3bxGY8HiRCIH3doFtQGYXKvYDD7_3Qcy0rFlSrYRGwXwMukDh7ryNDZGdQpndhCweKpsSOmIw75Pg0gS4vmDPbdgyv5E1hDbOuuLuCZaro1DRlQn811HuNPF47R6yyYvuxFBBkEluG9u4' \
#     --header 'accept: application/json' \
#     --header 'content-type: application/json' \
#     --data '{"asset_tag":"4063"}'

def Update(ID, dataIn, Date,serverURI,key):
    global requestcounter
    print("Request Counter: " + str(requestcounter))
    data = getDetailsByTag(serverURI, key, ID)
    #print(data.content)
    jsonData = json.loads(data.content)
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
def updateAssetModdel(server, token, id, model, tag):
        global requestcounter
        payload = {
            "model_id": model,
            "status_id": 2,
            "asset_tag": str(tag)
        }
        """Update asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Asset data 
        """
        uri = '/api/v1/hardware/'+str(id)
        server = server + uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token), 'accept': 'application/json'}
        results = requests.put(server, headers=headers, data=json.dumps(payload))
        requestcounter += 1
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

def update_SnipeIT(diviceList, testtypes,serverURI, key):

    for i in diviceList:
        print("-----------\nWorking on " + i + ": ")
        outData = ""
        divice = diviceList[i]
        for test in testtypes:
            try:
                divice[test]
                #print(divice[test])
                outData += test
                outData += " - Limit: " + divice[test]["Limit"]
                outData += " - Measurement: " + divice[test]["Measurement"]
                outData += " - Result: " + divice[test]["Result"]
                outData += "\n"
                #print(outData)
            except KeyError:
                outData += test + " - No Data\n"
                #print("Test: "+ test + " Not Found! Applying No Data")
                #print("Not Found")
        print("Updating Snipe-IT ID: " + i + "  and date: " + divice["date"] + " with the following data:\n" + outData)
        #print(divice["Date"])
        Update(i, outData, divice["date"],serverURI,key)