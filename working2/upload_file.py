import sys, os, random, shutil
import json
import requests
import hmac
import base64
import hashlib
import datetime


KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain"


def generateHMAC(payload, method, resource=""):
    fullpayload = method + "\n" + resource + "\n" + payload + "\n"
    digest = hmac.new(SECRET.encode('ascii'), msg=fullpayload.encode('ascii'), digestmod=hashlib.sha256).digest()
    signature = str(base64.b64encode(digest))[2:46]
    return signature


def upload(filename):
    date = datetime.datetime.utcnow().isoformat()
    AUTH = "ALTR " + KEY + ":" + generateHMAC(date, "POST")
    payload = open(filename, "rb").read()
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


#argv[1] is the filename to be uploaded, which is also epoch time
#argv[2] is if the file contains a face
"""
def upload(filename):
    token = str(random.randint(0, 3456788))
    shutil.copyfile(filename, "fake_blockchain/" + token)
    return token
"""

filename = "videos/" + sys.argv[1]
delete_file = filename + ".avi"
upload_file = filename + ".mp4"

os.remove(delete_file)
token = json.loads(upload(upload_file).text)["response"]["data"]["referenceToken"]
print(token)
os.remove(upload_file)

with open("fake_redis/" + sys.argv[1], "w") as file:
    file.write(token + " " + sys.argv[2])

