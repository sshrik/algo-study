const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

const inputSpliter = input => input.split(' ').map(Number);

const make2DArray = n => {
  const arr = new Array(n);

  for (let i = 0; i < n; i++) {
    arr[i] = [];
  }

  return arr;
};

const checkVisited = visited => {
  for (let i = 0; i < visited.length; i++) {
    if (visited[i] === 0) {
      return i;
    }
  }
  return -1;
};

const isBipartiteGraph = graph => {
  const VISITED = {
    NOT: 0,
    ONE: 1,
    TOW: 2,
  };

  const N = graph.length;
  const visited = new Array(N).fill(VISITED.NOT);
  const stack = [[0, VISITED.ONE]];

  while (true) {
    if (stack.length === 0) {
      if (checkVisited(visited) === -1) {
        break;
      } else {
        stack.push([checkVisited(visited), VISITED.ONE]);
      }
    }

    const [currentPosition, before] = stack.pop();

    const now = before === VISITED.ONE ? VISITED.TOW : VISITED.ONE;

    if (visited[currentPosition] === VISITED.NOT) {
      visited[currentPosition] = now;
    } else {
      continue;
    }

    for (let x = 0; x < graph[currentPosition].length; x += 1) {
      const adjIndex = graph[currentPosition][x];

      if (visited[adjIndex] === VISITED.NOT) {
        stack.push([adjIndex, now]);
      } else if (visited[adjIndex] === now) {
        return false;
      }
    }
  }

  return true;
};

const solution = input => {
  const K = Number(input[0]);
  let nextInputIndex = 1;

  for (let k = 0; k < K; k++) {
    const [V, E] = inputSpliter(input[nextInputIndex]);

    const graph = make2DArray(V);

    for (let e = 0; e < E; e++) {
      const [v1, v2] = inputSpliter(input[nextInputIndex + e + 1]);

      graph[v1 - 1].push(v2 - 1);
      graph[v2 - 1].push(v1 - 1);
    }

    console.log(isBipartiteGraph(graph) ? 'YES' : 'NO');

    nextInputIndex = nextInputIndex + E + 1;
  }
};

solution(input);
