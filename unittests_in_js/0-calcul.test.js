// unittesting module for 0-calcul.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

// Test cases
describe('calculateNumber', () => {
  it('should return the right number', () => {
    assert.strictEqual(2.7 + 5.3, 8);
  });
});
