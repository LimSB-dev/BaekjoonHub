function check(start, end, room) {
    const [hourStart, minuteStart] = start
    const [hourEnd, minuteEnd] = end
    
    for (let hour = hourStart; hour <= hourEnd; hour++) {
        if (hour !== hourEnd) {
            
        } else {
            
        }
    }
    
    return true
}

function getRoom(start, end, rooms) {
    
    for (let i = 0; i < rooms.length; i++) {
        const room = rooms[i]
        
        check(start, end, room)
    }
}

function solution(book_time) {
    let answer = 0;
    let rooms = new Array(1).fill(Array(24).fill(Array(60).fill(false)))
    const times = []
    
    book_time.forEach(time => {
        const start = time[0].slice(0,5).split(':').map(num => Number(num))
        const end = time[1].slice(0,5).split(':').map(num => Number(num))
        
        times.push([start, end])
    })
        
    times.map(time => {
        const [start, end] = time
        
        getRoom(start, end, rooms)
    })
    
    return answer;
}