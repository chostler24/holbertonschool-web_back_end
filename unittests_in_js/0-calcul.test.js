// unittesting module for 0-calcul.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

// Test cases
describe('calculateNumber', () => {
  it('should return the rounded sum of two positive numbers', () => {
    assert.strictEqual(calculateNumber(2.7, 5.3), 8);
  });

  it('should return the rounded sum of a positive number and a negative number', () => {
    assert.strictEqual(calculateNumber(2.7, -5.3), -2);
  });

  it('should return the rounded sum of two negative numbers', () => {
    assert.strictEqual(calculateNumber(-2.7, -5.3), -8);
  });

  it('should return the rounded sum of two large numbers', () => {
    assert.strictEqual(calculateNumber(9999999999.9, 8888888888.8), 18888888889);
  });

  it('should return 0 when both numbers are 0', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should handle rounding properly for decimal values', () => {
    assert.strictEqual(calculateNumber(2.4, 4.6), 7);
  });
});
