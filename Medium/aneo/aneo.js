let speed = parseInt(readline());
const lightCount = parseInt(readline());
const lights = [];
for (let i = 0; i < lightCount; i++) {
    lights.push(readline().split(' ').map(Number));
}


while (true) {
    const currentSpeed = speed;
    for([distance, duration] of lights) {
        const timeToArrive = 3.6 * distance / speed;
        if ((timeToArrive / duration) % 2 >= 1){
            speed--;
            break;
        }

    }
    if (currentSpeed === speed) break;
}

console.log(speed)