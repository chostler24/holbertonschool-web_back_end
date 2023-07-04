// 0-calcul.js module

const calculateNumber = (a, b) => {
    let aRound = Math.round(a);
    let bRound = Math.round(b);
    return aRound + bRound;
}

module.exports = calculateNumber;
