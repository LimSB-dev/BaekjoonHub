const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0], 10);
const A = [];
const B = [];
const C = [];
const D = [];

for (let i = 1; i <= N; i++) {
  const [a, b, c, d] = input[i].split(' ').map(Number);
  A.push(a);
  B.push(b);
  C.push(c);
  D.push(d);
}

const sumAB = new Map();
let result = 0;

// A[i] + B[j]의 모든 합을 구해서 Map에 저장 (그 합의 개수를 카운팅)
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    const sum = A[i] + B[j];
    sumAB.set(sum, (sumAB.get(sum) || 0) + 1);
  }
}

// C[k] + D[l]의 합이 -(A[i] + B[j])가 되는 경우를 찾음
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    const sum = -(C[i] + D[j]);
    if (sumAB.has(sum)) {
      result += sumAB.get(sum);
    }
  }
}

process.stdout.write(result + '\n');