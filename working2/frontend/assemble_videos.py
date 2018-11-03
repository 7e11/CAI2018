import os, shutil, time

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


def download(token):
    date = datetime.datetime.utcnow().isoformat()
    AUTH = "ALTR " + KEY + ":" + generateHMACDownload("GET\n" + token + "\n" + date + "\n")
    headers = {
        'Authorization': AUTH,
        'Content-Type': "application/octet-stream",
        'X-ALTR-DATE': date,
        'cache-control': "no-cache"
        }
    response = requests.request("GET", URL + token, headers=headers, stream=True)
    return response


template = """<h2>TIME: </h2><div class=FACE?><video loop width="640" height="480" controls>
  <source src="videos/INDEX.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video></div>"""

html_body = ""

indexes = os.listdir("../fake_redis")
indexes.sort()
for index in indexes:
    with open("../fake_redis/" + index) as file:
        token, contains_face = file.read().split(" ")
        html_body += template\
            .replace("INDEX", index)\
            .replace("TIME", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(index))))\
            .replace("FACE?", "hasface" if contains_face == "True" else "noface")

        with open("videos/" + index + ".mp4", "wb") as file:
            file.write(download(token).raw.read())

with open("template.html") as template:
    template = template.read().replace("BODY", html_body)
    with open("index.html", "w") as index:
        index.write(template)
