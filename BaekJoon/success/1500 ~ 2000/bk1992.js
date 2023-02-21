const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

function copmress(picture) {
  // picture = 2 x 2 array
  if (
    picture[0][0] === '1' &&
    picture[0][1] === '1' &&
    picture[1][0] === '1' &&
    picture[1][1] === '1'
  ) {
    return '1';
  }
  if (
    picture[0][0] === '0' &&
    picture[0][1] === '0' &&
    picture[1][0] === '0' &&
    picture[1][1] === '0'
  ) {
    return '0';
  }
  return '(' + picture[0][0] + picture[0][1] + picture[1][0] + picture[1][1] + ')';
}

function solution(input) {
  const N = Number(input[0]);
  const binaryPicture = input.slice(1).map(v => v.split('').map(v => v));

  let n = N;
  let tempPicture = binaryPicture;

  while (n > 1) {
    n /= 2;

    let compressedPicture = Array.from(Array(n), () => new Array(n));

    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < n; j += 1) {
        compressedPicture[i][j] = copmress([
          [tempPicture[i * 2][j * 2], tempPicture[i * 2][j * 2 + 1]],
          [tempPicture[i * 2 + 1][j * 2], tempPicture[i * 2 + 1][j * 2 + 1]],
        ]);
      }
    }

    tempPicture = compressedPicture;
  }

  return tempPicture[0][0];
}

console.log(solution(input));
