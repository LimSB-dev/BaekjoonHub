function solution(n) {
  return String(n).split('').map(num => +num).reduce((a, c) => a + c, 0);
}
