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

  it('should return correct status code', (done) => {
    request('http://localhost:7865/cart/12', (error, response, res) => {
      expect(response.statusCode).to.equal(200);
      expect(res).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 if id is not number', (done) => {
    request('http://localhost:7865/cart/whatevs', (error, response, res) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return the available payment methods', (done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });

  it('should return the welcome message with the username', (done) => {
    const userName = 'JohnDoe';
    request.post(
      {
        url: 'http://localhost:7865/login',
        json: true,
        body: { userName }
      },
      (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal(`Welcome ${userName}`);
        done();
      }
    );
  });
});
