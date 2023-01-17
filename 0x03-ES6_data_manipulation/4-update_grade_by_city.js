export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((data) => data.location === city)
    .map((data) => {
      const du = data;
      du.grade = 'N/A';
      for (const pro of newGrades) {
        if (du.id === pro.studentId) du.grade = pro.grade;
      }
      return du;
    });
}
