// https://www.acmicpc.net/problem/9466
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const getCycle = (start, selectResult, matched) => {
  // start 에서 시작해서 visited가 false인 것들에서 사이클을 찾는다.

  const stack = [start];
  const cycle = [];

  const visited = Array(selectResult.length).fill(false);

  while (stack.length > 0) {
    const now = stack.pop();
    const next = selectResult[now];

    if (matched[now]) {
      return [];
    }

    if (visited[now]) {
      if (cycle[0] === now) {
        return cycle;
      } else {
        return [];
      }
    } else {
      visited[now] = true;

      cycle.push(now);

      stack.push(next);
    }
  }

  return [];
};

const solution = input => {
  const T = Number(input[0]);

  for (let t = 0; t < T; t += 1) {
    const N = Number(input[t * 2 + 1]);
    const selectResult = input[t * 2 + 2].split(' ').map(v => Number(v) - 1);

    const matched = Array(N).fill(false);

    for (let n = 0; n < N; n += 1) {
      if (matched[n]) continue;

      const cycle = getCycle(n, selectResult, matched);

      for (let i = 0; i < cycle.length; i += 1) {
        matched[cycle[i]] = true;
      }
    }

    let count = 0;

    for (let i = 0; i < N; i += 1) {
      if (!matched[i]) count += 1;
    }

    console.log(count);
  }
};

solution(input);
