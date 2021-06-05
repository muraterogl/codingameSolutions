var inputs = readline().split(' ');
const h = parseInt(inputs[0]);
const w = parseInt(inputs[1]);
const n = parseInt(inputs[2]);
const alive = readline();
const dead = readline();
let cells = [];
for (let i = 0; i < h; i++) {
    const line = readline();
    cells.push(line);
}

for (let x = 0; x < n; x++) {
    let newCells = [];
    for (let i = 0; i < h; i++) {
        let newRow = [];
        for (let j = 0; j < w; j++) {
            let currentCell = cells[i][j];
            let neighborCount = 0;
            for(let k = Math.max(0, i-1); k < Math.min(h, i+2); k++) {
                for(let l = Math.max(0, j-1); l < Math.min(w, j+2); l++) {
                    if (cells[k][l] === "O") neighborCount++;
                }
            }
            if (currentCell === "O") {
                neighborCount -= 1;
                if (alive[neighborCount] === "0")
                    currentCell = "."
            }
            else{
                if (dead[neighborCount] === "1")
                    currentCell = "O"
            }
            newRow.push(currentCell);
        }
        newCells.push(newRow);
    }
    cells = newCells;
}

for(cell of cells)
    console.log(cell.join(""));
