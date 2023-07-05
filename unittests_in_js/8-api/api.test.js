// testing suite for api.js module

const request = require('request');
const { expect } = require('chai');


describe('Index Page', () => {
  it('should return the correct result', (done) => {
    request('http://localhost:7865', (error, response, res) => {
      expect(response.statusCode).to.equal(200);
      expect(res).to.equal('Welcome to the payment system');
      done();
      });
  });
});
