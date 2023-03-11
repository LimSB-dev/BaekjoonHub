function solution(n, m, x, y, r, c, k) {
  let answer = '';
  let dist = Math.abs(x - r) + Math.abs(y - c);
  k -= dist;
  
  if (k < 0 || k % 2 !== 0) {
    return "impossible";
  }

  let direction = {d: 0, l: 0, r: 0, u: 0};

  if (x > r) {
    direction['u'] += x - r;
  } else {
    direction['d'] += r - x;
  }

  if (y > c) {
    direction['l'] += y - c;
  } else {
    direction['r'] += c - y;
  }

  answer += 'd'.repeat(direction['d']);

  let d = Math.min(parseInt(k / 2), n - (x + direction['d']));
  answer += 'd'.repeat(d);
  direction['u'] += d;
  k -= 2 * d;

  answer += 'l'.repeat(direction['l']);
  let l = Math.min(parseInt(k / 2), y - direction['l'] - 1);
  answer += 'l'.repeat(l);
  direction['r'] += l;
  k -= 2 * l;

  answer += 'rl'.repeat(parseInt(k / 2));
  answer += 'r'.repeat(direction['r']);
  answer += 'u'.repeat(direction['u']);

  return answer;
}
