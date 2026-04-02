import json
import requests
import time
serverURI = "http://localhost:80"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZmY0NzVkYWU3Nzc2YTM5YWNjNWNjZjNiMTFmM2YwMGVjZjI0M2E4N2RiZWRkYWYxZGNlYzA4OTQ0MWZiOGI1ZDcyNWM5NWU1N2Q2YWZlYzAiLCJpYXQiOjE3NzM0MTczOTkuNjY5MTAzLCJuYmYiOjE3NzM0MTczOTkuNjY5MTA2LCJleHAiOjMwMzU3MjEzOTkuNjYzMzk4LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.mNyobe6Qc-epOdY2H1BFshG0GtdVg6XfYE7VVFBlTYzjUkA4Cf3lIMAGce_9egXiToVU2c4lXDtrtdxJuheDxhPiVp3UlDsF_ZzC6efDzNwL-JyPfBdQW0L92FgvJxFJoDva8wDihFTM0gYuW09uRGcg2SzhdkYuJgKIQJuMMsnqOnLkRO0LM6QA_bguMf_m_a19UeckD-FazY9SVEV7lTCukhP6VniOROToiXWzS5CJmQalsPCJRSlb7E_ZubI-QBP3YGEK6ao4x5Wh166KU3deeOX3TVZzsxDg21Q3JANow_nAEsdc35mXk1W_jKdC3bLUnP-79Rq2npxxvPku6H7P0d0nXXM7zpThxYHdFRzHcuByfd_URRWGm7-yHxlJQ0JW_2uE0exw3jme68betX8HKlCjicikktb99-Ybdd9PF9H52i20JTIgIx4wNhnQ2RtzlGmz5nks-BiICt-XOod2w6ij7HxX2B4IrUIHp_tf-CqB-btMjPQ4v0kwD-FiWHtpEmi7v38jj97uZkW2IkjzGzOoTSlHm9nP7C4DdL7GxVBhMHJVbkRpgxCH19ZkGYghgz7NiSo2ztvbkKTHmkCUmmiPINe-wYxmPTWDF2rukj81xq73lIJEPxkwD-ZvfX-HEauufOIhW8gKKogIaw5VCLYHLck7mVk9jxrtFMc"
requestcounter = 0
MaxCounter = 1980
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
        print(results)
        print("Error Below")
        #b'{"status":"error","messages":{"start_date":["The start date must be a valid date in YYYY-MM-DD format"],"completion_date":["The completion date field must match the format Y-m-d.","The completion date field must be a date after or equal to start date."]},"payload":null}'
        if(results.json().get("status") == "error"):
            #print("Error creating maintenance: " + str(results.json().get("messages")))
            print(results)
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
        if(requestcounter > MaxCounter):
            print("Request Counter: " + str(requestcounter) + " - Pausing for 60 seconds to avoid rate limit...")
            time.sleep(60)
            requestcounter = 0
        #print(results.content)
        #print("Error Below")
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
#     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTkwYmM2YjRmZGNjMjc3NzY4OWZkNTBjZDhiZGY5Zjk2MDA0YmIxZjI2Y2QxMDNkZTlkMjk2ZDlkNjA5ZmQ5ZjE3ZGM2NzAyMjQ0MjI4MzgiLCJpYXQiOjE3NzIyOTc3NDguNTc0MjM3LCJuYmYiOjE3NzIyOTc3NDguNTc0MjM4LCJleHAiOjMwMzQ2MDE3NDguNTcxMTAyLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.ap0_isUdId3dH8qGGVMrXQYFQUNjOqe_mjEK_Uq7QGtFZrkFXgeeJaTEOzkG9hU116vl_6vm_PBagA60KTNk_4IyZ0eLxk2PLpz8iRuy6M4Xy72RmoETUcluVVN-SKCK3cViNMuZ5Ldsm6ytV6k-PcOt-IuO6NnmirLbFOjYKszqR5I6wz2vQtLjvgk50vbVyNTUI0AMZ6CgffB_GV_LmZ0-oCeBMezXxS5ooBkHX5a7bQnZJMgtmdNyX9cqWjDvTib5IORRcgPmEWYw3WF39ac45fuax6WF77br7d2rfY06jJgwRe1M0heBVIIlq8qaflGWBTaDvWF2IL15OX6aDksm_6noTm0saZIx1-8AOEkNmCTF4Y70V2CN8gNhgg8c5ivFGQyXc99eGMa6Lz1LO0NXLVqnU1p0y5n6uxm0uSnZxNed9dpLGaEbuN2PcY2Oxwk8gXRLExH85nbV5-7_H-u8Map2yp0ZOCfdAqX4G3LOxP4XUAVtzZOjVSTWPe_cpMX7bk6AqmF4dFh0qk-QVeV6wbukMp3bxGY8HiRCIH3doFtQGYXKvYDD7_3Qcy0rFlSrYRGwXwMukDh7ryNDZGdQpndhCweKpsSOmIw75Pg0gS4vmDPbdgyv5E1hDbOuuLuCZaro1DRlQn811HuNPF47R6yyYvuxFBBkEluG9u4' \
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


def update_SnipeIT(diviceList, testtypes):

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
        print("Updating Snipe-IT ID: " + i + "  and date: " + divice["Date"] + " with the following data:\n" + outData)
        #print(divice["Date"])
        Update(i, outData, divice["Date"])