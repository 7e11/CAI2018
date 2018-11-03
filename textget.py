import requests
import hmac
import base64
import hashlib
import datetime

KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
REF = "chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain/"

def generateHMAC(payload):
    print("HMAC Payload: ", payload)
    # secureHash = hashlib.sha256(fullpayload, SECRET)
    # secureHash = hmac.new(bytearray(SECRET, 'utf-8'), bytearray(fullpayload, 'utf-8'), hashlib.sha256).digest()
    # base64.b64encode(secureHash).decode()
    digest = hmac.new(bytes.fromhex(SECRET), msg=bytearray(payload, 'utf-8'), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    return str(signature)

date = datetime.datetime.now().isoformat();
AUTH = "ALTR " + KEY + ":" + generateHMAC("GET\n" + REF + "\n" + date + "\n")
print(AUTH)
#
headers = {
    'Authorization': AUTH,
    'Content-Type': "application/json",
    'X-ALTR-DATE': date,
    'cache-control': "no-cache"
    }
#
response = requests.request("GET", URL + REF, headers=headers)

print(response.text)
