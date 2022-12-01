const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n')[0].split(' ');

const N = Number(input[0]);

const pow2 = [];

let i = 0;

while (Math.pow(2, i) < N) {
  pow2.push(Math.pow(2, i));
  i += 1;
}
pow2.push(Math.pow(2, i));

const K = Number(input[1]);

function solution() {
  let sum = 0;

  for (let k = 0; k < K; k += 1) {
    let n = 0;

    // console.log(`${k}회차`);

    for (n = 0; n < pow2.length; n += 1) {
      if (pow2[n] >= N - sum) {
        sum += pow2[n];

        // console.log(`${pow2[n]} 물을 넣을 예정, 넣은 뒤 물의 양 ${sum}`);

        if (sum === N) {
          return 0;
        }
        if (k + 1 === K) {
          return sum - N;
        } else {
          if (n === 0) return -1;
          let m = n;
          sum -= pow2[n];

          for (m = n; m > -1; m -= 1) {
            if (sum + pow2[m] < N) {
              break;
            }
          }

          sum += pow2[m];
          // console.log(`넣고 보니 아직 통이 여유, ${pow2[m]} 물을 넣음, 넣은 뒤 물의 양 ${sum}`);
        }
        break;
      }
    }
  }
}

console.log(solution());
