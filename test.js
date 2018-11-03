let KEY="ALTR-24E95DD903235BE18B130C1CAA0923ED";
let SECRET = "4df873715bde1fdf27d751619f0aca3d199";
//***//,
var crypto = require('crypto-js');

function generateHMAC( payload, method, resource) {
    console.log("HMAC Payload: ", payload);
    console.log("HMAC Method: ", method);
    let fullpayload = method  + "\n\n" + (resource ? resource:"") + "\\\n" + payload + "\\\n";
    console.log(fullpayload);
    let hash = CryptoJS.HmacSHA256(fullpayload,SECRET);
    return CryptoJS.enc.Base64.stringify(hash);
}
pm.environment.set(\altrkey\, KEY); ,
var date =(new Date()).toISOString();,
pm.environment.set(\altrauth\, \ALTR \ + KEY + \:\ + generateHMAC(date, pm.request.method)); ,
pm.environment.set(\altrdate\, date);