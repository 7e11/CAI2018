import requests

import requests

# url = "https://dgl-hackathon.dev.altr.com/api/v1/chain/chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e"
API_KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED"
SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39"

headers = {
    'Authorization': "{{altrauth}}",
    'Content-Type': "application/json",
    'X-ALTR-DATE': "{{altrdate}}",
    'cache-control': "no-cache",
    'Postman-Token': "1c52a41a-9850-4999-a70f-7de183d9048c"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)