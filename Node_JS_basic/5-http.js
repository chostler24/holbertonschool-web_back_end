const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const { method, url } = req;

  if (method === 'GET') {
    if (url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello Holberton School!');
    } else if (url === '/students') {
      const databasePath = 'database.csv';

      countStudents(databasePath)
        .then(() => {
          res.writeHead(200, { 'Content-Type': 'text/plain' });
          res.end('This is the list of our students\n');
        })
        .catch((error) => {
          res.writeHead(500, { 'Content-Type': 'text/plain' });
          res.end(`${error.message}\n`);
        });
    } else {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Not found\n');
    }
  } else {
    res.writeHead(405, { 'Content-Type': 'text/plain' });
    res.end('Method not allowed\n');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
