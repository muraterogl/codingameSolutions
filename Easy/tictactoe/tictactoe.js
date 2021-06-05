let board = [];

for (let i = 0; i < 3; i++) {
    board = board.concat(readline().split(""));
}

const tester = (board) => {
    const winningPoss = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]];
    for (let [a, b, c] of winningPoss) {
        if (board[a] === "O" && board[b] === "O" && board[c] === "O")
            return true;
    }
    return false;
};

for(let i = 0; i < 9; i++) {
    if(board[i] === "."){
        board[i] = "O";
        if (tester(board)){
            for(let j = 0; j < 9; j+=3){
                console.log(board.slice(j, j+3).join(""));
            }
            process.exit();
        }
        else{
            board[i]=".";
        }
    }
}

console.log("false");