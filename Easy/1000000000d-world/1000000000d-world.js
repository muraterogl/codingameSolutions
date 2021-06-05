let a = readline().split(" ").map(Number);
let b = readline().split(" ").map(Number);
let result = 0;

while (a.length>0) {
    let factor = Math.min(a[0], b[0]);
    result += factor * a[1] * b[1];
    a[0] -= factor;
    b[0] -= factor;
    if (a[0] === 0) a = a.splice(2);
    if (b[0] === 0) b = b.splice(2);
}

console.log(result);