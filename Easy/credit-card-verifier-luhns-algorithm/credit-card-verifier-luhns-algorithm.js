const verifier = (card) => {
    card = card.replace(/ /g, "").split("").map(Number);
    let secondStep = 0;
    for (let i = 0; i < card.length; i+=2) {
        const factor = card[i] * 2;
        secondStep += factor < 10 ? factor : factor - 9;
    }
    let thirdStep = 0;
    for (let i = 1; i < card.length; i+=2) {
        thirdStep += card[i];
    }
    let fourthStep = secondStep + thirdStep;
    console.log(fourthStep % 10 === 0 ? "YES" : "NO");
};

const n = parseInt(readline());
for (let i = 0; i < n; i++) {
    const card = readline();
    verifier(card);
}