const N = parseInt(readline());
const L = parseInt(readline());
let cells = [];
let candles = [];

for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    let rowHold = [];
    for (let j = 0; j < N; j++) {
        if (inputs[j] === "C") candles.push([j, i]);
        rowHold.push(0);
    }
    cells.push(rowHold);
}

candles.forEach(candle => {
    for (let i = 0; i < N; i++){
        for (let j = 0; j < N; j++){
            cells[j][i] = Math.max(cells[j][i], Math.max(0, L - Math.max(Math.abs(candle[0]-j), Math.abs(candle[1]-i))));

        }
    }
});

let darkCount = 0;

cells.forEach(row => row.forEach(cell => {
    if (cell === 0) darkCount++;
}));

console.log(darkCount); 
