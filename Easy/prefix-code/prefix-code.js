
const n = parseInt(readline());
var d = {};
for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    const b = inputs[0];
    const c = parseInt(inputs[1]);
    d[b]=String.fromCharCode(c);
}
var s = readline();
var result = "";
var index = 0;
while(s){
    var l = s.length;
    for (var key in d){
        if(s.startsWith(key)){
            result+=d[key];
            s=s.slice(key.length);
        }
    }
    if(l==s.length){
        console.log(`DECODE FAIL AT INDEX ${index}`);
        return;
    }
    index+=l-s.length;
}

console.log(result);
 
