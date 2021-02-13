var inputs = readline().split(' ');
const w = parseInt(inputs[0]);
const h = parseInt(inputs[1]);
const countX = parseInt(inputs[2]);
const countY = parseInt(inputs[3]);

var xs = [0, ...readline().split(' ').map(Number),w];
var ys = [0, ...readline().split(' ').map(Number),h];


var dx = []
var dy = []

xs.forEach((a,i)=>{
    xs.slice(i+1).map(x=>dx.push(x-a))
})
ys.forEach((a,i)=>{
    ys.slice(i+1).map(y=>dy.push(y-a))
})

var squares = 0

dx.forEach(x=>{
    squares+=dy.filter(y=>y==x).length
})
console.log(squares) 
