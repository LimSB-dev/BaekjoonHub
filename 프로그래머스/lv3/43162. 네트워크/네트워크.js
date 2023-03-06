// 유니온 파인드 알고리즘
class UnionFind {
    constructor(size) {
        this.parent = new Array(size)
        this.rank = new Array(size)
        
        // Initialize each element as a separate set
        for (let i =0; i < size; i++) {
            this.parent[i] = i
            this.rank[i] = 0
        }
    }
    
    // Find the parent of a node and perform path compression
    find(x) {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x])
        }
        return this.parent[x]
    }
    
    // Union two sets by rank
    union(x, y) {
        let px = this.find(x)
        let py = this.find(y)
        
        if (px === py) {
            return false
        }
        
        if (this.rank[px] < this.rank[py]) {
            this.parent[px] = py
        } else if (this.rank[px] > this.rank[py]) {
            this.parent[py] = px
        } else {
            this.parent[py] = px
            this.rank[px]++
        }
        
        return true
    }
    
    size() {
        console.log(this.parent)
        const parentSet = new Set(this.parent)
        
        return parentSet.size
    }
}


function solution(n, computers) {
    let answer = 0
    
    const uf = new UnionFind(n)
    
    computers.forEach(computer => {
        const [x, y] = computer
        
        uf.union(x, y)
    })
    
    console.log(uf)
    
    return uf.size()
}