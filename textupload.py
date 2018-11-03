import requests
import hmac
import base64
import hashlib
import datetime

def generateHMAC(payload, method, resource = ""):
    print("HMAC Payload: ", payload)
    print("HMAC Method: ", method)
    fullpayload = method + "\n" + resource + "\n" + payload + "\n"
    print(fullpayload)
    # secureHash = hashlib.sha256(fullpayload, SECRET)
    secureHash = hmac.new(SECRET, fullpayload, hashlib.sha256)
    base64.b64encode(secureHash).decode()
    return secureHash

# url = "https://dgl-hackathon.dev.altr.com/api/v1/chain/chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e"
KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain"
date = datetime.datetime.now().isoformat();
AUTH = "ALTR " + KEY + ":" + generateHMAC(date, POST)
print(AUTH)
#
# headers = {
#     'Authorization': "{{altrauth}}",
#     'Content-Type': "application/json",
#     'X-ALTR-DATE': "{{altrdate}}",
#     'cache-control': "no-cache",
#     'Postman-Token': "1c52a41a-9850-4999-a70f-7de183d9048c"
#     }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)


# pm.environment.set("altrkey", KEY)
# var
# date = (new Date()).toISOString()
# pm.environment.set("altrauth", "ALTR " + KEY + ":" + generateHMAC(date, pm.request.method))
# pm.environment.set("altrdate", date)
