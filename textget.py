import requests
import hmac
import base64
import hashlib
import datetime

KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
REF = "chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain/"


def generateHMACDownload(payload):
    digest = hmac.new(SECRET.encode('ascii'), msg=payload.encode('ascii'), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature


def getData(reference):
    date = datetime.datetime.utcnow().isoformat()
    AUTH = "ALTR " + KEY + ":" + generateHMACDownload("GET\n" + reference + "\n" + date + "\n")
    headers = {
        'Authorization': AUTH,
        'Content-Type': "application/octet-stream",
        'X-ALTR-DATE': date,
        'cache-control': "no-cache"
        }
    response = requests.request("GET", URL + reference, headers=headers)
    return response

# print(getData("chain_1d2d2c4277c0a730b977acc18e67382f36e083d2b699c4d866cf9afef4f4271f").content)
print(getData("chain_fedd85ba7e4a8bd58008436517bdacf80ff8110534793929ba234f503a7b9799").raw)
# print(getData("chain_ae93eb73e2f12018398de90877dfe18ac01593ff3fecdf0b39bf85ac69595bb2").content)
# print(getData(REF).text)
# print(getData("chain_e172bd299e0150864f1885b1aaf9f8c35811d075b9f4235e3993ab33faf2b2be").content)