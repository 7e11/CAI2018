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
    date = datetime.datetime.utcnow().isoformat()
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

# with open("arbol_0.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
# print(putData(encoded_string).content)

data = open("arbol_0.jpg", "rb").read()
# data = "jfdksljhfksdjfkldsjfkldsjfkldsjfkldjkfldsjkfldsjklfjdsklfjdskljflds"
# print(putData(data).text) #chain_759911ac1a3776e2d3b7499509327de13237a18a8a2e533f5f09dc989ab872bf
# chain_1d2d2c4277c0a730b977acc18e67382f36e083d2b699c4d866cf9afef4f4271f
# image encoded as a base64 string.