// https://www.acmicpc.net/problem/3190
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

const Direction = {
  EAST: 0,
  WEST: 1,
  SOUTH: 2,
  NORTH: 3,
};

const EMPTY = 0;
const APPLE = 1;
const SNAKE = 2;

const canMove = (x, y, direction, N) => {
  switch (direction) {
    case Direction.EAST:
      return y + 1 < N;
    case Direction.WEST:
      return y - 1 >= 0;
    case Direction.SOUTH:
      return x + 1 < N;
    case Direction.NORTH:
      return x - 1 >= 0;
  }
};

const nextPosition = (x, y, direction) => {
  switch (direction) {
    case Direction.EAST:
      return [x, y + 1];
    case Direction.WEST:
      return [x, y - 1];
    case Direction.SOUTH:
      return [x + 1, y];
    case Direction.NORTH:
      return [x - 1, y];
  }
};

const move = (x, y, snakeList, direction, board) => {
  const N = board.length;

  if (canMove(x, y, direction, N)) {
    const [nextX, nextY] = nextPosition(x, y, direction);

    if (board[nextX][nextY] === APPLE) {
      board[nextX][nextY] = SNAKE;
      snakeList.push([nextX, nextY]);
      return true;
    } else if (board[nextX][nextY] === EMPTY) {
      snakeList.push([nextX, nextY]);
      board[nextX][nextY] = SNAKE;

      const [endX, endY] = snakeList.shift();

      board[endX][endY] = EMPTY;

      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
};

const calcDirection = (direction, turn) => {
  if (turn === 'L') {
    switch (direction) {
      case Direction.EAST:
        return Direction.NORTH;
      case Direction.WEST:
        return Direction.SOUTH;
      case Direction.SOUTH:
        return Direction.EAST;
      case Direction.NORTH:
        return Direction.WEST;
    }
  } else {
    switch (direction) {
      case Direction.EAST:
        return Direction.SOUTH;
      case Direction.WEST:
        return Direction.NORTH;
      case Direction.SOUTH:
        return Direction.WEST;
      case Direction.NORTH:
        return Direction.EAST;
    }
  }
};

const solution = input => {
  const N = Number(input[0]);

  const board = Array.from(Array(N), () => Array(N).fill(EMPTY));

  board[0][0] = SNAKE;

  const snakeList = [[0, 0]];

  let direction = Direction.EAST;

  const K = Number(input[1]);

  for (let k = 0; k < K; k++) {
    const [x, y] = input[k + 2].split(' ').map(Number);

    board[x - 1][y - 1] = APPLE;
  }

  const L = Number(input[K + 2]);

  let nowSecond = 0;

  const turnList = {};

  for (let l = 0; l < L; l++) {
    const [second, turn] = input[K + l + 3].split(' ');

    turnList[Number(second)] = turn;
  }

  while (true) {
    const [x, y] = snakeList[snakeList.length - 1];

    if (move(x, y, snakeList, direction, board)) {
      nowSecond += 1;
    } else {
      break;
    }
    if (turnList[nowSecond]) {
      direction = calcDirection(direction, turnList[nowSecond]);
    }
  }

  console.log(nowSecond + 1);
};

rl.on('line', line => {
  input.push(line);
}).on('close', () => {
  solution(input);
});
