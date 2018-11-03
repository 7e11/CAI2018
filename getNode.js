var KEY="ALTR-24E95DD903235BE18B130C1CAA0923ED";
var SECRET="4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39";
var URL="https://dgl-hackathon.dev.altr.com/api/v1/chain/";
var REF = "chain_618f5f6485a9c93f970846193207027c08d0634962460e3e46069692daa70d3e";
var REQUEST_METHOD = "GET"

var request = require("request");

var CryptoJS = require('crypto-js');
function generateHMAC( payload, method, resource)
{
    console.log("HMAC Payload: ", payload);
    console.log("HMAC Method:", method);
    var fullpayload = method  + "\n" + (resource ? resource:"") + "\n" + payload + "\n";
    console.log(fullpayload);
    var hash = CryptoJS.HmacSHA256(fullpayload,SECRET);
    return CryptoJS.enc.Base64.stringify(hash);
}

// pm.environment.set("altrkey", KEY);
var date =(new Date()).toISOString();
// pm.environment.set("altrauth", "ALTR " + KEY + ":" + generateHMAC(date, pm.request.method, pm.request.url.variables.get("referenceToken")));
// pm.environment.set("altrdate", date);

var options = { method: 'GET',
  url: URL + REF,
  headers:
   { 'Postman-Token': 'a69982be-d345-4d9e-bbf7-4e816396d51f',
     'cache-control': 'no-cache',
     'X-ALTR-DATE': date,
     'Content-Type': 'application/json',
     Authorization: "ALTR " + KEY + ":" + generateHMAC(date, REQUEST_METHOD, REF)  } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});