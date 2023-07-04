// unittesting suite for 6-payment_token.js module

const assert = require('assert');
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./getPaymentTokenFromAPI');

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise with data when success is true', async () => {
    const response = await getPaymentTokenFromAPI(true);
    assert.deepStrictEqual(response, { data: 'Successful response from the API' });
  });

  it('should return a resolved promise without data when success is false', async () => {
    const response = await getPaymentTokenFromAPI(false);
    assert.strictEqual(response, undefined);
  });
});
