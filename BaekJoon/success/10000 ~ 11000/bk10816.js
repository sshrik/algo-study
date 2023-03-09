const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

const solution = input => {
  const numberCard = input[1].split(' ');

  const cardCount = {};

  const cardList = input[3].split(' ');

  cardList.forEach(v => (cardCount[v] = 0));

  numberCard.forEach(v => {
    if (cardCount.hasOwnProperty(v)) {
      cardCount[v] += 1;
    }
  });

  let result = '';

  cardList.forEach(v => {
    result += `${cardCount[v]} `;
  });

  console.log(result);
};

rl.on('line', line => {
  input.push(line);
}).on('close', () => {
  solution(input);
});
