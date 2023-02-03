function solution(k, tangerine) {
  let answer = 0;
  let types = {};

  tangerine.forEach((type) => {
    if (types[type]) {
      types[type] = types[type] + 1;
    } else {
      types[type] = 1;
    }
  });

  let result = [];

  Object.entries(types).map((type) => {
    result.push(type[1]);
  });

  result.sort((a, b) => b - a);

  for (let i = 0; i < result.length; i++) {
    if (k > 0) {
      k -= result[i];
      answer++;
    } else {
      break;
    }
  }

  return answer;
}