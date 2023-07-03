// 3-read_file_async.js module

const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  if (!fs.existsSync(path)) {
    reject(new Error('Cannot load the database'));
  }

  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    } else {
      let lines = data.split('\n');

      // Calculate the number of students in each field
      lines = lines.filter((line) => line !== '').slice(1);
      console.log(`Number of students: ${lines.length}`);

      const field = lines.map((line) => line.split(',')[3]);

      const eachField = [...new Set(field)];

      eachField.forEach((fieldName) => {
        const studentsPerField = lines
          .filter((line) => line.endsWith(fieldName))
          .map((line) => {
            const split = line.split(',');
            return split[0];
          });
        console.log(
          `Number of students in ${fieldName}: ${studentsPerField.length}. List: ${studentsPerField.join(', ')}`,
        );
      });

      resolve();
    }
  });
});

module.exports = countStudents;
