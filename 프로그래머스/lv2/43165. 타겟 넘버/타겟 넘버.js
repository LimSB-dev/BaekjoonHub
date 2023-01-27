function dfs(startIndex, numbers, target) {
  return (function dfsRecursive(num, index) {
    if (index === numbers.length) {
      if (num === target) {
        return 1;
      } else {
        return 0;
      }
    }
    let num1 = num + numbers[index];
    let num2 = num - numbers[index];

    return dfsRecursive(num1, index + 1) + dfsRecursive(num2, index + 1);
  })(0, startIndex);
}

class Queue {
  constructor() {
    this.items = [];
  }
  enqueue(elem) {
    return this.items.push(elem);
  }
  dequeue() {
    return this.items.shift();
  }
  isEmpty() {
    return this.items.length === 0;
  }
}

function bfs(startIndex, numbers, target) {
  const queue = new Queue();
  queue.enqueue([numbers[startIndex], -numbers[startIndex]]);
  let index = startIndex + 1;
  let answer = 0;

  while (!queue.isEmpty()) {
    let list = queue.dequeue();

    if (index !== numbers.length) {
      let newList = [];

      for (let num of list) {
        newList.push(num + numbers[index]);
        newList.push(num - numbers[index]);
      }

      index++;
      queue.enqueue(newList);
    } else {
      // console.log(list, queue);
      for (let num of list) {
        if (num === target) {
          answer++;
        }
      }
    }
  }

  return answer;
}

function solution(numbers, target) {
  // DFS
  // let answer = dfs(0, numbers, target);

  // BFS
  let answer = bfs(0, numbers, target);

  return answer;
}