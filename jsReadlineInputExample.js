const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

const solution = input => {};

rl.on('line', line => {
  input.push(line);
}).on('close', () => {
  solution(input);
});
