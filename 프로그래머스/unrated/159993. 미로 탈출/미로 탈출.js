class Queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }

    enqueue(element) {
        this.queue[this.rear++] = element;
    }

    dequeue() {
        const element = this.queue[this.front];
        delete this.queue[this.front++];
        return element;
    }

    isEmpty() {
        return this.rear === this.front;
    }
}

const INF = 999999999

function solution(maps) {
    let answer = 0;
    
    // 2D의 너비와 높이
    const width = maps[0].length
    const height = maps.length
    
    // 상 하 좌 우
    const dr = [-1, 1, 0, 0]
    const dc = [0, 0, -1, 1]
    
    // matrix 생성
    const matrix = maps.map(row => row.split(''))
    
    /** matrix에서 target의 row, col를 Array 형태로 반환. */
    const quest = (target) => {
        for (let row = 0; row < height; row++) {
            for (let col = 0; col < width; col++) {
                if (maps[row][col] === target) {
                    return [row, col]
                }
            }
        }    
    }
    
    /** bfs 탐색을 하며 현재 위치에서 target까지 이동 시 최소 시간을 반환 */
    const bfs = (row, col, target) => {        
        // 방문 배열 생성
        let visited = Array.from(Array(height), () => new Array(width).fill(false))
        
        // queue 생성
        let queue = new Queue()
        
        // 시작 queue 추가
        queue.enqueue([row, col, 0])

        // 시작 지점 방문 처리
        visited[row][col] = true
        
        // queue가 빌 때까지 반복
        while (!queue.isEmpty()) {
            
            // dequeue
            let [r, c, value] = queue.dequeue()
            
            // 종료 조건
            if (matrix[r][c] === target) {
                return value
            }
            
            for (let direction = 0; direction < 4; direction++) {
                const nr = r + dr[direction]
                const nc = c + dc[direction]
                
                // matrix 내부 확인
                if (nr < 0 || height <= nr || nc < 0 || width <= nc) continue
                
                // 벽 확인
                if (matrix[nr][nc] === 'X') continue
                
                // 방문 확인
                if (visited[nr][nc]) continue
                
                // 방문처리
                visited[nr][nc] = true
                
                // enqueue
                queue.enqueue([nr, nc, value + 1])
            }
        }
        // 종료 조건에 도달하지 못했을 경우
        return -INF
    }
    
    // 시작지점에서 레버까지 최소 이동 시간
    const [rowStart, colStart] = quest('S')
    answer += bfs(rowStart, colStart, 'L')
    
    if (answer < 0) return -1
    
    // 레버지점에서 출구까지 최소 이동 시간
    const [rowLever, colLever] = quest('L')
    answer += bfs(rowLever, colLever, 'E')
    
    if (answer < 0) return -1
    
    return answer;
}