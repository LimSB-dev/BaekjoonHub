function solution(num, k) {
  const index = String(num).split('').findIndex(n => Number(n) === k);
  return index === -1 ? -1 : index + 1;
}
