// 0-calcul.js module

const calculateNumber = (a, b) => {
    const aRound = Math.round(a);
    const bRound = Math.round(b);
    if (isNaN(a) || isNaN(b)) throw TypeError('Args must be numbers');
    return aRound + bRound;
}

module.exports = calculateNumber;
