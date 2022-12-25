function solution(n) {
  let answer = 0;

  for (let i = 1; i <= n / 2; i++) {
    let sumValue = 0;

    for (let j = 0; j <= n; j++) {
      sumValue += i + j;

      if (sumValue === n) {
        answer++;
      } else if (sumValue > n) {
        break;
      }
      //   console.log(sumValue);
    }
  }

  if (n >= 1) {
    answer++;
  }
  return answer;
}