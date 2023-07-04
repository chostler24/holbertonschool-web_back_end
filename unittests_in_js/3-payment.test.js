// unittesting suite for 3-payment.js module

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
    it('should call Utils.calculateNumber with correct arguments', () => {
      const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

      sendPaymentRequestToApi(100, 20);

      expect(calculateNumberSpy.calledOnceWith('SUM', 100, 20)).to.be.true;

      calculateNumberSpy.restore();
    });
  });
