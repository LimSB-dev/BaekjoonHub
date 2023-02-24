class Heap {
    constructor() {
        this.heap = [null]
    }
    
    push(number) {
        this.heap.push(number)
        
        let currentIndex = this.heap.length - 1
        let parentIndex = Math.floor(currentIndex / 2)
        
        while (parentIndex >= 1 && this.heap[currentIndex] < this.heap[parentIndex]) {
            [this.heap[currentIndex], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[currentIndex]]
            
            currentIndex = parentIndex
            parentIndex = Math.floor(currentIndex / 2)
        }
    }
    
    findMin() {
        if (this.heap.length <= 1) {
            return null;
        }

        if (this.heap.length === 2) {
            return this.heap.pop();
        }

        const min = this.heap[1];
        this.heap[1] = this.heap.pop();

        let currentIndex = 1;
        let leftChildIndex = 2 * currentIndex;
        let rightChildIndex = 2 * currentIndex + 1;

        while (
            (this.heap[leftChildIndex] && this.heap[currentIndex] > this.heap[leftChildIndex]) ||
            (this.heap[rightChildIndex] && this.heap[currentIndex] > this.heap[rightChildIndex])
        ) {
            if (this.heap[leftChildIndex] < this.heap[rightChildIndex] || !this.heap[rightChildIndex]) {
                [this.heap[currentIndex], this.heap[leftChildIndex]] = [this.heap[leftChildIndex], this.heap[currentIndex]];
                currentIndex = leftChildIndex;
            } else {
                [this.heap[currentIndex], this.heap[rightChildIndex]] = [this.heap[rightChildIndex], this.heap[currentIndex]];
                currentIndex = rightChildIndex;
            }

            leftChildIndex = 2 * currentIndex;
            rightChildIndex = 2 * currentIndex + 1;
        }
        
        return min
    }

    findMax() {
        const maxHeap = new Heap();
        
        for (const number of this.heap.slice(1)) {
          maxHeap.push(-number);
        }
        
        const absMax = -maxHeap.findMin();
        
        const index = this.heap.indexOf(absMax)
        if (index > -1) this.heap.splice(index, 1)
        return absMax
     }
    

    size() {
        return this.heap.length - 1;
    }
    
    result() {
        return [this.findMax(), this.findMin()]
    }
}

function solution(operations) {
    const heap = new Heap()
    
    operations.forEach((operation) => {
        const [command, number] = operation.split(' ')

        if (command === 'I') {
            // 힙 삽입
            heap.push(Number(number))
        } else if (command === 'D') {
            if (number === '1') {
                // 최대값 제거
                heap.findMax()
            } else if (number === '-1') {
                // 최소값 제거
                heap.findMin()
            }
        }
    })
    
    
    let answer = heap.result()
    
    if (answer[0] === null || answer[1] === null) {
        answer = [0,0]
    }
    return answer
}