import requests
import hmac
import base64
import hashlib
import datetime

KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain"


def generateHMAC(payload, method, resource = ""):
    fullpayload = method + "\n" + resource + "\n" + payload + "\n"
    digest = hmac.new(SECRET.encode('ascii'), msg=fullpayload.encode('ascii'), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature


def putData(data):
    date = datetime.datetime.utcnow().isoformat();
    AUTH = "ALTR " + KEY + ":" + generateHMAC(date, "POST")
    payload = data
    # payload = "{\"hello\": \"world\", \"this is\": \"chainAPI\"}"
    headers = {
        'Authorization': AUTH,
        'Content-Type': "application/octet-stream",
        'X-ALTR-DATE': date,
        'cache-control': "no-cache",
        'Postman-Token': "1c52a41a-9850-4999-a70f-7de183d9048c"
        }
    response = requests.request("POST", URL, data=payload, headers=headers)
    return response


print(putData("{\"hello\": \"world\", \"this is\": \"chainAPIFromPython\"}").content)