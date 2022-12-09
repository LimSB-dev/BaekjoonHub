const fs = require("fs");
// const input = fs.readFileSync("./input.txt").toString().split("\n");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [maxValue, r, c] = [0, 1, 1];

for (let row = 0; row < 9; row++) {
  input[row] = [...input[row].split(" ")];
  for (let col = 0; col < 9; col++) {
    const value = Number(input[row][col]);
    if (maxValue < value) {
      maxValue = value;
      r = row + 1;
      c = col + 1;
    }
  }
}

console.log(maxValue);
console.log(r, c);