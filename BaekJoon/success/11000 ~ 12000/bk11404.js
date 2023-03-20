// https://www.acmicpc.net/problem/11404
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const solution = input => {
  const N = Number(input[0]);
  const M = Number(input[1]);

  const graph = Array.from(Array(N), () => Array(N).fill(Infinity));

  for (let i = 0; i < M; i += 1) {
    const [start, end, cost] = input[i + 2].split(' ').map(Number);

    if (graph[start - 1][end - 1] > cost) {
      graph[start - 1][end - 1] = cost;
    }
  }

  const dist = Array.from(Array(N), () => Array(N).fill(Infinity));

  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      if (i === j) {
        dist[i][j] = 0;
      } else {
        dist[i][j] = graph[i][j];
      }
    }
  }

  for (let k = 0; k < N; k += 1) {
    for (let i = 0; i < N; i += 1) {
      for (let j = 0; j < N; j += 1) {
        if (dist[i][j] > dist[i][k] + dist[k][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }

  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      if (dist[i][j] === Infinity) {
        dist[i][j] = 0;
      }
    }
  }

  for (let i = 0; i < N; i += 1) {
    let result = '';

    for (let j = 0; j < N; j += 1) {
      result += `${dist[i][j]} `;
    }

    console.log(result);
  }
};

solution(input);
