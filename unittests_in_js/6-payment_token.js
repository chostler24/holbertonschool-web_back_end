// 6-payment_token.js module

const getPaymentTokenFromAPI = (success) => {
    if (typeof success !== 'boolean') throw TypeError('success must be boolean');
    if (success) {
        return Promise.resolve({ data: 'Successful response from the API' });
    } else {
        return Promise.resolve();
    }
}

module.exports = getPaymentTokenFromAPI;
