// 2-read_file.js module

const fs = require('fs');

const countStudents = (file) => {
  try {
    const file = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

    // Calculate the number of students in each field
    const fields = {};
    let totalStudents = 0;

    for (const line of lines) {
      const [firstName, lastName, field] = line.split(',');

      if (field) {
        totalStudents++;

        if (fields[field]) {
          fields[field].push(firstName);
        } else {
          fields[field] = [firstName];
        }
      }
    }

    // Log the results
    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      const studentsInField = fields[field].length;
      const studentList = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${studentsInField}. List: ${studentList}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
