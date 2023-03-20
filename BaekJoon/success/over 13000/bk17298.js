// https://www.acmicpc.net/problem/17298

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const solution = input => {
  const N = Number(input[0]);

  const arr = input[1].split(' ').map(Number);

  const stack = [0];

  const result = new Array(N).fill(-1);

  for (let i = 1; i < N; i++) {
    while (stack.length > 0) {
      const top = arr[stack[stack.length - 1]];

      if (top < arr[i]) {
        result[stack.pop()] = arr[i];
      } else {
        stack.push(i);
        break;
      }
    }
    if (stack.length === 0) {
      stack.push(i);
    }
  }

  console.log(result.join(' '));
};

solution(input);
