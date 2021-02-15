const L = parseInt(readline());
const N = parseInt(readline());
let results = [[0, L]];

for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const st = parseInt(inputs[0]);
    const ed = parseInt(inputs[1]);
    let newResults = [];

    results.forEach(result => {
        if (ed <= result[0] || st >= result[1]){
            newResults.push(result);
        }
        else if (st <= result[0] && ed >= result[0] && ed < result[1]){
            newResults.push([ed, result[1]]);
        }
        else if (st > result[0] && ed < result[1]){
            newResults.push([result[0], st]);
            newResults.push([ed, result[1]]);
        }
        else if (st > result[0] && st < result[1] && ed >= result[1]){
            newResults.push([result[0], st]);
        }
    });

    results = newResults

}

results.forEach(result => console.log(`${result[0]} ${result[1]}`))

if (results.length === 0) console.log("All painted")
 
