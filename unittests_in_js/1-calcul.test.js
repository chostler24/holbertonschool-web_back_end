// unittesting suite for 1-calcul.js module

const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
    it('positive numbers', () => {
      assert.equal(calculateNumber('SUM', 1, 3), 4);
      assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
      assert.equal(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
    });

    it('negative numbers', () => {
      assert.equal(calculateNumber('SUM', -1, -3), -4);
      assert.equal(calculateNumber('SUBTRACT', -1, -3), 2);
      assert.equal(calculateNumber('DIVIDE', -1, -3), 0.3333333333333333);
    });

    it('positive and negative numbers', () => {
      assert.equal(calculateNumber('SUM', -1, 3), 2);
      assert.equal(calculateNumber('SUBTRACT', -1, 3), -4);
      assert.equal(calculateNumber('DIVIDE', -1, 3), -0.3333333333333333);
    });

    it('zeros', () => {
      assert.equal(calculateNumber('SUM', 0, 0), 0);
      assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
      assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
    });
  });
