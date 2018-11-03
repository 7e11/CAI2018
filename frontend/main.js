let reference_token = "whatever";
let date = new Date();
let payload = 'GET\n' + referenceToken + '\n' + date + '\n';
let API_KEY = "ALTR-24E95DD903235BE18B130C1CAA0923ED";
let SECRET = "4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39";
let url = "https://dgl-hackathon.dev.altr.com/api/v1/chain/chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e/" + reference_token;
let request_headers = {
    "X-ALTR-DATE": date,
    "Authorization": "ALTR " + API_KEY + ":" + base64(hmac-sha256(payload, SECRET))
};


$.ajax({
    url: url,
    headers: request_headers
}).done(function(data) {
    console.log(data);
});