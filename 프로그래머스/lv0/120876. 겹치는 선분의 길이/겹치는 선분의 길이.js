function solution(lines) {
  const counting = lines.reduce((arr, [s, e]) => {
    for (let i = s; i < e; i++) {
      arr[i] = arr[i] ? arr[i] + 1 : 1
    } 
    return arr
  }, {})

  const answer = Object.values(counting).filter(cnt => cnt > 1).length
  
  return answer
}