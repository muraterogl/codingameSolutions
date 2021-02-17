var inputs = readline().split(' ');
const w = parseInt(inputs[0]);
const h = parseInt(inputs[1]);
let extracted = "";
for (let i = 0; i < h; i++) {
    var inputs = readline().split(' ');
    for (let j = 0; j < w; j++) {
        const pixel = parseInt(inputs[j]);
        const bin = pixel.toString(2);
        extracted += bin[bin.length-1];
    }
}
while(extracted.length % 8 != 0) extracted = "0" + extracted

let result = "";

for (let i = 0; i < extracted.length; i+=8){
    result += String.fromCharCode(parseInt(extracted.slice(i, i+8), 2));
}
console.log(result); 
