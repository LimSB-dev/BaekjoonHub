const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const V = parseInt(input[0], 10);
const graph = Array.from({ length: V + 1 }, () => []);

for (let i = 1; i <= V; i++) {
  const line = input[i].split(' ').map(Number);
  const u = line[0];
  for (let j = 1; j < line.length - 1; j += 2) {
    const v = line[j];
    const w = line[j + 1];
    graph[u].push([v, w]);
  }
}

let maxDistance = 0;
let farthestNode = 0;

// DFS 함수 정의
function dfs(node, distance, visited) {
  visited[node] = true;

  if (distance > maxDistance) {
    maxDistance = distance;
    farthestNode = node;
  }

  for (const [nextNode, weight] of graph[node]) {
    if (!visited[nextNode]) {
      dfs(nextNode, distance + weight, visited);
    }
  }
}

// 1. 임의의 노드(1번)에서 가장 먼 노드를 찾음
let visited = Array(V + 1).fill(false);
dfs(1, 0, visited);

// 2. 그 노드로부터 가장 먼 노드를 찾음
maxDistance = 0;
visited = Array(V + 1).fill(false);
dfs(farthestNode, 0, visited);

console.log(maxDistance);