// 2-read_file.js module

const db = require('./database.csv');

module.exports = function countStudents(path) {
    if (!db) {
        throw error('Cannot load the databse')
    } else {
        process.stdin.read(db);
        console.log('Number of students: ${}');
    }
}
