let grid = []

//Creating grid while checking row errors
for (let i = 0; i < 9; i++) {
    row = readline().split(' ').map(i => parseInt(i));
    if (row.length === [...new Set(row)].length) grid.push(row);
    else {
        console.log("false");
        throw new Error();
    }
    
}

//Checking column errors
for (let i = 0; i < 9; i++) {
    let column = new Set();
    for (let j = 0; j < 9; j++) {
        column.add(grid[j][i]);
    }

    if(column.size !== 9){
        console.log("false");
        throw new Error();
    }
}

//Checking subgrid errors
for (let i = 0; i < 9; i+=3) {
    
    for (let j = 0; j < 9; j+=3) {
        let subgrid = new Set();

        for(let k = i; k < i+3; k++){
            for(let l = j; l < j+3; l++){
                subgrid.add(grid[k][l]);
            }
        }

        if(subgrid.size !== 9){
            console.log("false");
            throw new Error();
        }
    }
    
}

console.log("true");
 
