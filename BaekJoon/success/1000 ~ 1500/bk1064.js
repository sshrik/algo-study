const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n')[0].split(' ');

const pointOne = { x: Number(input[0]), y: Number(input[1]) };
const pointTwo = { x: Number(input[2]), y: Number(input[3]) };
const pointThree = { x: Number(input[4]), y: Number(input[5]) };

function getInclination(p1, p2) {
  return { x: p1.x - p2.x, y: p1.y - p2.y };
}

function compareInclination(i1, i2) {
  if (i1.x * i2.y > i2.x * i1.y) return 1;
  else if (i1.x * i2.y < i2.x * i1.y) return -1;
  else return 0;
}

function isInclinationSame(i1, i2) {
  return compareInclination(i1, i2) === 0;
}

function isOnOneLine(p1, p2, p3) {
  const inclinationOneToTwo = getInclination(p1, p2);
  const inclinationTwoToThree = getInclination(p2, p3);
  const inclinationThreeToOne = getInclination(p3, p1);

  return (
    isInclinationSame(inclinationOneToTwo, inclinationTwoToThree) ||
    isInclinationSame(inclinationTwoToThree, inclinationThreeToOne) ||
    isInclinationSame(inclinationThreeToOne, inclinationOneToTwo)
  );
}

function getLength(p1, p2) {
  return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
}

if (isOnOneLine(pointOne, pointTwo, pointThree)) {
  console.log('-1.0');
} else {
  const lineOneToTwo = getLength(pointOne, pointTwo);
  const lineTwoToThree = getLength(pointTwo, pointThree);
  const lineThreeToOne = getLength(pointThree, pointOne);

  const squareLengthList = [
    (lineOneToTwo + lineTwoToThree) * 2,
    (lineTwoToThree + lineThreeToOne) * 2,
    (lineThreeToOne + lineOneToTwo) * 2,
  ];

  squareLengthList.sort((a, b) => a - b);

  console.log(squareLengthList[2] - squareLengthList[0]);
}
