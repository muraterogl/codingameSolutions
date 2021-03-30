const width = parseInt(readline());
const height = parseInt(readline());
const nodes = [];

for (let i = 0; i < height; i++) {
    nodes.push(readline());
}

for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
        if (nodes[i][j] === "0") {
            const output = [j,i];

            let rigthNotFound = true;
            for (let k = j+1; k < width; k++) {
                if (nodes[i][k] === "0") {
                    output.push(k, i);
                    rigthNotFound = false;
                    break;
                }
            }
            if (rigthNotFound) {
                output.push(-1, -1);
            }


            let bottomNotFound = true;
            for (let k = i+1; k < height; k++) {
                if (nodes[k][j] === "0") {
                    output.push(j, k);
                    bottomNotFound = false;
                    break;
                }
            }
            if (bottomNotFound) {
                output.push(-1, -1);
            }

            console.log(output.map(i => i.toString()).join(" "));
        }
    }
}

