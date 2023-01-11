class StackQueue {
    constructor(queue) {
        this.queue = queue ? queue : []
        this.front = 0
        this.rear = queue ? queue.length : 0
    }
    
    enqueue(val) {
        this.queue[this.rear++] = val
    }
    
    dequeue() {
        const val = this.queue[this.front]
        delete this.queue[this.front++]
        return val
    }
    
    pop() {
        const val = this.queue[--this.rear]
        delete this.queue[this.rear]
        return val
    }
    
    size() {
        return this.rear - this.front
    }
    
    weight() {
        return this.queue[this.rear - 1] + this.queue[this.front]
    }
}

function solution(people, limit) {
    const sorted = people.sort((a, b) => a - b)
    const queue = new StackQueue(sorted)
    let answer = 0
    
    while (queue.size() > 0) {
        const n = queue.size()
        const weight = queue.weight()
        if (weight <= limit) {
            queue.dequeue()
            queue.pop()
        } else {
            queue.pop()
        }
        
        answer++
    }
    
    return answer
}