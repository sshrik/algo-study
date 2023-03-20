// https://www.acmicpc.net/problem/1874

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const solution = input => {
  const N = Number(input[0]);

  const stack = [];

  const result = [];

  let now = 1;

  for (let nextInput = 1; nextInput <= N; nextInput++) {
    const next = Number(input[nextInput]);

    if (stack.length === 0 || stack[stack.length - 1] < next) {
      stack.push(now);
      result.push('+');
      now += 1;
      nextInput -= 1;
    } else if (stack[stack.length - 1] === next) {
      stack.pop();
      result.push('-');
    } else {
      console.log('NO');
      return;
    }
  }

  console.log(result.join('\n'));
};

solution(input);
