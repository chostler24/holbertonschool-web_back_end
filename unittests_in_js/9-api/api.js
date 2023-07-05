// api.js module

const express = require('express');

const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const cartier = req.params.id;
  if (isNaN(cartier)) {
    res.status(404).send('Cart id must be number');
  } else {
    res.send(`Payment methods for cart ${cartier}`);
  };
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
