const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const testCaseNumber = 3;
let totalIndex = 0;

for (let t = 0; t < testCaseNumber; t += 1) {
  const integerNumber = Number(input[totalIndex]);

  let sumAmount = BigInt(0);

  for (let i = totalIndex + 1; i < totalIndex + integerNumber + 1; i += 1) {
    sumAmount += BigInt(input[i]);
  }

  if (sumAmount === BigInt(0)) console.log(0);
  else if (sumAmount < 0) console.log("-");
  else console.log("+");

  totalIndex += integerNumber + 1;
}
