const n = parseInt(readline());
const arrays = {};
const arrayOffsets = {};
for (let i = 0; i < n; i++) {
    let [identifier, rest] = readline().split("[");
    [offset, rest] = rest.split("..");
    let [_, values] = rest.split(" = ");
    values = values.split(" ");
    arrayOffsets[identifier] = parseInt(offset);
    arrays[identifier] = values;
}
let x = readline();

while(x.includes("["))
    x = x.replace(/([^\[\]]+)\[(-?\d+)\]/, (_, identifier, value) => {
        value = parseInt(value) - arrayOffsets[identifier];
        return arrays[identifier][value];
    });

console.log(x);