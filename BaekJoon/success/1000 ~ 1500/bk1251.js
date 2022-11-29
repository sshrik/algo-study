const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n')[0];

function stringReverse(str) {
  return str.split('').reverse().join('');
}

function processWord(word, firstIndex, lastIndex) {
  const chunkOne = stringReverse(word.slice(0, firstIndex));
  const chunkTwo = stringReverse(word.slice(firstIndex, lastIndex));
  const chunkThree = stringReverse(word.slice(lastIndex));

  return chunkOne + chunkTwo + chunkThree;
}

function dfs(word) {
  const wordDictionary = [];

  for (let firstIndex = 1; firstIndex < word.length - 1; firstIndex += 1) {
    for (let lastIndex = firstIndex + 1; lastIndex < word.length; lastIndex += 1) {
      wordDictionary.push(processWord(word, firstIndex, lastIndex));
    }
  }

  wordDictionary.sort();

  return wordDictionary[0];
}

console.log(dfs(input));
