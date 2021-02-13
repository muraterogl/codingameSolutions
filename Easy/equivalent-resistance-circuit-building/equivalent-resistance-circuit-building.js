const N = parseInt(readline());
const resistors = {};

//Resistor names and values
for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const name = inputs[0];
    const R = parseInt(inputs[1]);
    resistors[name] = R;
}
const circuit = readline();

const findElements = (resString) => {
    let elements = [];
    let paranthesis = [];
    let hold = "";

    for(const character of resString){

        hold += character;

        if(character === " "){

            //If paranthesis' are matched, append hold without last space to elements
            if(paranthesis.length === 0){
                elements.push(hold.slice(0, -1));
                hold = "";
            }
        }
        else if(character === "(" || character === "["){
            paranthesis.push(character);
        }
        else if(character === ")" || character === "]"){
            paranthesis.pop();
        }
    }

    if(hold !== ""){
        elements.push(hold);
    }
    return elements;
};

const findRes = (resString) => {
    
    if(resString in resistors){
        return resistors[resString];
    }

    else{
        const elements = findElements(resString.slice(2,-2));

        //Series Connection
        if(resString[0] === "("){
            return elements.map(element => findRes(element)).reduce((element1,element2) => element1 + element2);
        }
        //Parallel Connection
        else{
            return 1/elements.map(element => 1/findRes(element)).reduce((element1,element2) => element1 + element2);
        }
    }
};

console.log(findRes(circuit).toFixed(1)); 
