//index.js module

const express = require('express');
const app = express();

const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

app.get('/', AppController.index);

app.get('/students', StudentsController.index);

app.get('/students/:major', StudentsController.getByMajor);

module.exports = app;
