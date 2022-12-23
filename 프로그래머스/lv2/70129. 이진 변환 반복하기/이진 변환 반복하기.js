function solution(s) {
  let answer = [0, 0];

  while (s !== "1") {
    let cnt = 0;
    for (let i = 0; i < s.length; ++i) {
      if (s[i] === "0") {
        cnt++;
      }
    }
    
    s = s.replaceAll("0", "");

    answer[0] += 1;
    answer[1] += cnt;
    s = String(s.length.toString(2));
  }

  return answer;
}