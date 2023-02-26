// https://www.acmicpc.net/problem/16928

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const END = 99;
const START = 0;

function init(input) {
  const [N, M] = input[0].split(' ').map(v => +v);

  const map = new Array(100).fill(0);

  for (let n = 0; n < N; n += 1) {
    const [from, to] = input[n + 1].split(' ').map(v => +v);
    map[from - 1] = to - 1;
  }

  for (let m = 0; m < M; m += 1) {
    const [from, to] = input[m + N + 1].split(' ').map(v => +v);
    map[from - 1] = to - 1;
  }

  return map;
}

function bfs(map, start = START, end = END) {
  const visited = new Array(100).fill(false);

  const queue = [[start, 0]];

  while (queue.length) {
    const [current, count] = queue.shift();

    if (visited[current]) continue;
    visited[current] = true;

    for (let dice = 1; dice < 7; dice += 1) {
      const next = current + dice;

      if (visited[next]) continue;

      if (next === end) {
        return count + 1;
      }
      if (map[next]) {
        queue.push([map[next], count + 1]);
      } else {
        queue.push([next, count + 1]);
      }
    }
  }

  return -1;
}

function solution(input) {
  const map = init(input);

  return bfs(map, START, END);
}

console.log(solution(input));
