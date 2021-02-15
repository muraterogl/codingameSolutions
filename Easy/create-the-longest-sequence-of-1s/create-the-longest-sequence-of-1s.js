const b = readline();
let counts = [];
for (let i = 0; i < b.length; i++) {
    let newBits = b.slice(0,i) + "1" + b.slice(i+1,b.length);
    counts.push(Math.max(...newBits.match(/1+/g).map(m => m.length)));
}
console.log(Math.max(...counts));
 
