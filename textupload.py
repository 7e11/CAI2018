import requests
import hmac
import base64
import hashlib
import datetime

KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain"

def generateHMAC(payload, method, resource = ""):
    print("HMAC Payload: ", payload)
    print("HMAC Method: ", method)
    fullpayload = method + "\n" + resource + "\n" + payload + "\n"
    print(fullpayload)
    # secureHash = hashlib.sha256(fullpayload, SECRET)
    # secureHash = hmac.new(bytearray(SECRET, 'utf-8'), bytearray(fullpayload, 'utf-8'), hashlib.sha256).digest()
    # base64.b64encode(secureHash).decode()
    digest = hmac.new(bytes.fromhex(SECRET), msg=bytearray(payload, 'utf-8'), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature

# url = "https://dgl-hackathon.dev.altr.com/api/v1/chain/chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e"
date = datetime.datetime.now().isoformat()
AUTH = "ALTR " + KEY + ":" + generateHMAC(date, "POST")
print(AUTH)
#
headers = {
    'Authorization': AUTH,
    'X-ALTR-DATE': date,
    'Content-Type': ''
    }
#
response = requests.request("POST", URL, headers=headers, data="hello how are you")
#
print(response.text)


# pm.environment.set("altrkey", KEY)
# var
# date = (new Date()).toISOString()
# pm.environment.set("altrauth", "ALTR " + KEY + ":" + generateHMAC(date, pm.request.method))
# pm.environment.set("altrdate", date)