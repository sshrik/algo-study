const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const studentList = [...new Array(30)].map(() => false);

input.forEach((studentNumber) => {
  studentList[Number(studentNumber) - 1] = true;
});

studentList.forEach((isSubmit, index) => {
  if (!isSubmit) console.log(index + 1);
});
