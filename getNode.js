var KEY="ALTR-24E95DD903235BE18B130C1CAA0923ED";
var SECRET="4df873715bde1fdf27d751619f0aca3d199fcc32dce112b988ce078287a76a39";
var URL="https://dgl-hackathon.dev.altr.com/api/v1/chain/";

var crypto = require('crypto-js');
function generateHMAC( payload, method, resource)
{
    console.log("HMAC Payload: ", payload);
    console.log("HMAC Method:", method);
    var fullpayload = method  + "\n" + (resource ? resource:"") + "\n" + payload + "\n";
    console.log(fullpayload);
    var hash = CryptoJS.HmacSHA256(fullpayload,SECRET);
    return CryptoJS.enc.Base64.stringify(hash);

}

pm.environment.set("altrkey", KEY);
var date =(new Date()).toISOString();
pm.environment.set("altrauth", "ALTR " + KEY + ":" + generateHMAC(date, pm.request.method, pm.request.url.variables.get("referenceToken")));
pm.environment.set("altrdate", date);