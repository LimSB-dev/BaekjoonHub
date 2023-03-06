function solution(n, works) {
  let total = works.reduce((acc, cur) => acc + cur, 0)
  
  // 모든 일을 처리할 수 있을 경우
  if (total <= n) return 0
  
  // 우선순위 큐로 구현된 max heap을 이용하여 작업량을 정렬
  const pq = new MaxHeap()
  works.forEach(work => pq.insert(work))
  
  // 가장 큰 작업량부터 하나씩 처리
  while (n > 0) {
    const maxWork = pq.extract()
    pq.insert(maxWork - 1)
    n--
  }
  
  // 야근 피로도 계산
  let fatigue = pq.container.reduce((acc, cur) => acc + cur ** 2, 0)
  return fatigue
}

class MaxHeap {
  constructor() {
    this.container = []
  }
  
  insert(data) {
    this.container.push(data);
    let idx = this.container.length - 1
    
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2)
      if (this.container[idx] <= this.container[parentIdx]) break
      
      const temp = this.container[idx]
      this.container[idx] = this.container[parentIdx]
      this.container[parentIdx] = temp
      idx = parentIdx
    }
  }
  
  extract() {
    const max = this.container[0]
    if (this.container.length === 1) {
      return this.container.pop()
    }
    
    this.container[0] = this.container.pop()
    let idx = 0
    const length = this.container.length
    
    while (true) {
      const leftChildIdx = idx * 2 + 1
      const rightChildIdx = idx * 2 + 2
      let swapIdx = idx
      
      if (leftChildIdx < length && this.container[leftChildIdx] > this.container[swapIdx]) {
        swapIdx = leftChildIdx
      }
      
      if (rightChildIdx < length && this.container[rightChildIdx] > this.container[swapIdx]) {
        swapIdx = rightChildIdx
      }
      
      if (swapIdx === idx) break
      
      const temp = this.container[idx]
      this.container[idx] = this.container[swapIdx]
      this.container[swapIdx] = temp
      idx = swapIdx
    }
    
    return max
  }
}
