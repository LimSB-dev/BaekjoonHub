const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0], 10);
const board = [];
for (let i = 1; i <= N; i++) {
  board.push(input[i].split(' ').map(Number));
}

let maxBishops = [0, 0];
let diagonal1 = Array(2 * N).fill(false);
let diagonal2 = Array(2 * N).fill(false);

function placeBishop(depth, color, count) {
  maxBishops[color] = Math.max(maxBishops[color], count);

  for (let i = depth; i < N * N; i++) {
    const row = Math.floor(i / N);
    const col = i % N;

    if ((row + col) % 2 !== color || board[row][col] === 0 || diagonal1[row - col + N - 1] || diagonal2[row + col]) {
      continue;
    }

    diagonal1[row - col + N - 1] = true;
    diagonal2[row + col] = true;
    placeBishop(i + 1, color, count + 1);
    diagonal1[row - col + N - 1] = false;
    diagonal2[row + col] = false;
  }
}

placeBishop(0, 0, 0); // 흑색 칸
placeBishop(0, 1, 0); // 백색 칸

console.log(maxBishops[0] + maxBishops[1]);