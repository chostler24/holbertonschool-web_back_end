// testing suite for api.js module

const chai = require('chai');
const expect = chai.expect;

const app = require('./api');

describe('Index Page', () => {
  it('should return a 200 status code', (done) => {
    chai
      .request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('should return the correct result', (done) => {
    chai
      .request(app)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
