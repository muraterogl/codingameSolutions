var inputs = readline().split(' ');
const w = parseInt(inputs[0]);
const h = parseInt(inputs[1]);
var inputs = readline().split(' ');
const startRow = parseInt(inputs[0]);
const startCol = parseInt(inputs[1]);
const n = parseInt(readline());
let results = [];
for (let i = 0; i < n; i++) {
    let currentMap = [];
    for (let j = 0; j < h; j++) {
        currentMap.push(readline().split``);
    }

    let currentX = startCol;
    let currentY = startRow;
    let length = 0;
    let roundCount = 0;

    while (currentMap[currentY][currentX]!=="T" && currentMap[currentY][currentX]!==".") {
        
        if(currentMap[currentY][currentX] === "^"){
            currentY--;
            length++;
        }
        else if(currentMap[currentY][currentX] === "v"){
            currentY++;
            length++;
        }
        else if(currentMap[currentY][currentX] === "<"){
            currentX--;
            length++;
        }
        else if(currentMap[currentY][currentX] === ">"){
            currentX++;
            length++;
        }

        if(currentX === startCol && currentY === startRow){
            roundCount++;
        }

        if(roundCount > 0 || currentX >= w || currentY >= h)
        {
            results.push([i, Infinity]);
            break;
        }

        if(! "^v<>".includes(currentMap[currentY][currentX])){
            if(currentMap[currentY][currentX]!=="T"){
                length = Infinity;
            }
            results.push([i, length]);
        }
    }
}

if(results.every(result => result[1] === Infinity)){
    console.log("TRAP");
}
else{
    results = results.sort((result1, result2) => result1[1]-result2[1]);
    console.log(results[0][0]);
}
 
