// StudentsController.js module

import readDatabase from '../utils.js';

class StudentsController {
    static getAllStudents(req, res) {
        const student = readDatabase('../../database.csv');
        let returnString = 'This is the list of our students';
        student.CS.name.sort();
        student.SWE.names.sort();
        res.send(`${returnString}\nNumber of students in CS: ${student.CS.names.length}. List: ${students.CS.names.join(', ')}\n${returnString}\nNumber of students in SWE: ${student.SWE.names.length}. List: ${students.SWE.names.join(', ')}`);
    };

    // static getAllStudentsByMajor(req, res) {
    //     const { major } = req.params;
    // }
};
