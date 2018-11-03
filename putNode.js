var KEY="ALTR-24E95DD903235BE18B130C1CAA0923ED";
var SECRET="4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39";
var URL="https://dgl-hackathon.dev.altr.com/api/v1/chain";
var REQUEST_METHOD = "POST";
var request = require("request");
//***//
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

var date =(new Date()).toISOString();

var options = { method: 'POST',
  url: URL,
  headers:
   { 'Postman-Token': 'cfc498fd-5765-4668-8222-5d54a84db58d',
     'cache-control': 'no-cache',
     'X-ALTR-DATE': date,
     'Content-Type': 'application/json',
     Authorization: "ALTR " + KEY + ":" + generateHMAC(date, REQUEST_METHOD) },
  body: { hello: 'world', 'this is': 'A JS Hack' },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
