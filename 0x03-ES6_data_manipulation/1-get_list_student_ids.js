export default function getListStudentIds(arg) {
  if (!(arg instanceof Array)) {
    return [];
  }
  return arg.map((student) => student.id);
}
