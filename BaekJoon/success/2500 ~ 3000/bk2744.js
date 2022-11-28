const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n")[0];

const lowercase = "abcdefghijklmnopqrstuvwxyz";

let result = "";

for (let i = 0; i < input.length; i += 1) {
  if (lowercase.includes(input[i])) result += input[i].toUpperCase();
  else result += input[i].toLowerCase();
}

console.log(result);
