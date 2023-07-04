// 1-calcul.js module

const calculateNumber = (type, a, b) => {
    const aRound = Math.round(a);
    const bRound = Math.round(b);
    let type = 'SUM' | 'SUBTRACT' | 'DIVIDE';
    if (isNaN(a) || isNaN(b)) throw TypeError('Args a, b must be numbers');
    if (typeof type !== 'string') throw TypeError('Arg type must be string');
    // if (bRound === 0) throw Error('Error');
    if (type === 'SUM') {
        return aRound + bRound;
    } else if (type === 'SUBTRACT') {
        return aRound - bRound;
    } else if (type === 'DIVIDE') {
        if (bRound === 0) {
            return 'Error';
        } else {
            return aRound / bRound;
        };
    };
}

module.exports = calculateNumber;
