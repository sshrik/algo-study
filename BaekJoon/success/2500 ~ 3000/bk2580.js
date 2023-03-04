// https://www.acmicpc.net/problem/2580

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on('line', line => {
  input.push(line);
}).on('close', () => {
  const sudokuMap = input.map(v => v.split(' ').map(v => +v));

  console.log(
    solution(sudokuMap)
      .map(v => v.join(' '))
      .join('\n')
  );
});

const getCandidate = (inputMap, row, col) => {
  const candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9];

  // get row candidate

  for (let x = 0; x < 9; x += 1) {
    if (inputMap[row][x] !== 0 && candidate.indexOf(inputMap[row][x]) !== -1) {
      candidate.splice(candidate.indexOf(inputMap[row][x]), 1);
    }
  }

  // get col candidate

  for (let y = 0; y < 9; y += 1) {
    if (inputMap[y][col] !== 0 && candidate.indexOf(inputMap[y][col]) !== -1) {
      candidate.splice(candidate.indexOf(inputMap[y][col]), 1);
    }
  }

  // get square candidate

  const squareRow = Math.floor(row / 3) * 3;
  const squareCol = Math.floor(col / 3) * 3;

  for (let y = squareRow; y < squareRow + 3; y += 1) {
    for (let x = squareCol; x < squareCol + 3; x += 1) {
      if (inputMap[y][x] !== 0 && candidate.indexOf(inputMap[y][x]) !== -1) {
        candidate.splice(candidate.indexOf(inputMap[y][x]), 1);
      }
    }
  }

  return candidate;
};

const findZero = inputMap => {
  for (let y = 0; y < 9; y += 1) {
    for (let x = 0; x < 9; x += 1) {
      if (inputMap[y][x] === 0) {
        return [y, x];
      }
    }
  }

  return [-1, -1];
};

const solution = sudokuMap => {
  const answerMap = sudokuMap.map(v => [...v]);

  const [fy, fx] = findZero(answerMap);

  if (fy === -1) return answerMap;

  const stack = [[[fy, fx], getCandidate(answerMap, fy, fx), -1]];

  while (stack.length > 0) {
    const [currentPos, candidate, index] = stack.pop();

    const [y, x] = currentPos;

    if (index === candidate.length - 1) {
      answerMap[y][x] = 0;
      continue;
    }

    const nextIndex = index + 1;
    const nextValue = candidate[nextIndex];

    answerMap[y][x] = nextValue;

    const [nextY, nextX] = findZero(answerMap);

    if (nextY === -1) {
      return answerMap;
    }

    stack.push([currentPos, candidate, nextIndex]);
    stack.push([[nextY, nextX], getCandidate(answerMap, nextY, nextX), -1]);
  }

  return answerMap;
};
