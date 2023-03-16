// https://www.acmicpc.net/problem/15654
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const getNextCandidate = (numbers, stack, nowUsed) => {
  const N = numbers.length;

  const candidate = [];

  const used = stack.map(([nowIndex, _1, _2]) => nowIndex);

  used.push(nowUsed);

  for (let i = 0; i < N; i += 1) {
    if (used.indexOf(i) === -1) {
      candidate.push(i);
    }
  }

  return candidate;
};

const printStack = (stack, numbers) => {
  let result = '';

  for (let i = 1; i < stack.length; i += 1) {
    const [nowIndex, _1, _2] = stack[i];

    result += `${numbers[nowIndex]} `;
  }

  console.log(result);
};

const solution = input => {
  const [_, M] = input[0].split(' ').map(Number);

  const numbers = input[1]
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);

  const stack = []; // [nowIndex, nextCandidate, selectedCandidateIndex]

  stack.push([-1, getNextCandidate(numbers, stack, -1), -1]);

  while (stack.length > 0) {
    const [nowIndex, candidate, nextIndex] = stack.pop();

    if (nextIndex + 1 === candidate.length) {
      continue;
    }

    stack.push([nowIndex, candidate, nextIndex + 1]);

    const nextNowIndex = candidate[nextIndex + 1];
    const nextCandidate = getNextCandidate(numbers, stack, nextNowIndex);

    stack.push([nextNowIndex, nextCandidate, -1]);

    if (stack.length === M + 1) {
      printStack(stack, numbers);
      stack.pop();
    }
  }
};

solution(input);
