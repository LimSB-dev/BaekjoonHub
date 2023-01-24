function solution(n, left, right) {
  return new Array(right - left + 1).fill(0).reduce((acc, _, i) => {
    acc.push(Math.max((i + left) % n, parseInt((i + left) / n)) + 1);
    return acc;
  }, []);
}