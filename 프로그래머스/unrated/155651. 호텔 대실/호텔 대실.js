/** 객실 예약 상태로 변경 후 객실 반환 */
function reservate(start, end, room) {
    const [hourStart, minuteStart] = start
    let [hourEnd, minuteEnd] = end
    
    // 10분 청소
    minuteEnd = minuteEnd + 9
    
    if (minuteEnd >= 60) {
        if (hourEnd === 23) {
            minuteEnd = 59
        } else {
            hourEnd = hourEnd + 1
            minuteEnd = minuteEnd - 60
        }
    }
    
    for (let hour = hourStart; hour <= hourEnd; hour++) {
        if (hourStart === hourEnd) {
            for (let i = minuteStart; i <= minuteEnd; i++) {
                room[hour][i] = true
            }
        }
        else if (hour === hourStart && hour !== hourEnd) {
            for (let i = minuteStart; i < 60; i++) {
                room[hour][i] = true
            }
        } else if (hour !== hourStart && hour === hourEnd) {
            for (let i = 0; i <= minuteEnd; i++) {
                room[hour][i] = true
            }
        } else {
            for (let i = 0; i < 60; i++) {
                room[hour][i] = true
            }
        }
    }
    
    return room
}

/** 주어진 예약시간으로 현재 객실을 예약 가능하면 true 반환 */
function check(start, end, room) {
    const [hourStart, minuteStart] = start
    const [hourEnd, minuteEnd] = end
    
    for (let hour = hourStart; hour <= hourEnd; hour++) {
        if (hourStart === hourEnd) {
            for (let i = minuteStart; i <= minuteEnd; i++) {
                if (room[hour][i]) return false
            }
        }
        else if (hour === hourStart && hour !== hourEnd) {
            for (let i = minuteStart; i < 60; i++) {
                if (room[hour][i]) return false
            }
        } else if (hour !== hourStart && hour === hourEnd) {
            for (let i = 0; i <= minuteEnd; i++) {
                if (room[hour][i]) return false
            }
        } else {
            for (let i = 0; i < 60; i++) {
                if (room[hour][i]) return false
            }
        }
    }
    
    return true
}

/** 현재 객실들의 모든 시간을 탐색하며 예약이 가능할 경우 예약 후 객실들 반환 */ 
function getRoom(start, end, rooms) {
    for (let i = 0; i < rooms.length; i++) {
        let room = rooms[i]
        
        // 예약 가능할 경우
        if (check(start, end, room)) {
            
            // 예약 후 객실 반환
            room = reservate(start, end, room)
            
            // 객실 모음에 현재 객실을 예약된 상태로 변환
            rooms[i] = room
            
            // 객실 모음을 반환
            return rooms
        }
    }
    
    // 모든 방이 예약이 불가능할 경우 빈 객실 생성
    let room = new Array(24).fill().map(() => new Array(60).fill(false))
    
    // 빈 객실에 현재 예약 시간 예약
    room = reservate(start, end, room)

    // 객실 모음에 예약을 마친 객실 추가
    rooms.push(room)
    
    // 객실 모음을 반환
    return rooms
}

function solution(book_time) {
    let answer = 0
    // 얕은 복사를 피하는 객실의 모임 배열
    let rooms = new Array(1).fill().map(() => new Array(24).fill().map(() => new Array(60).fill(false)))
    // 예약 시간을 담을 배열
    const times = []
    
    // 예약 시간을 2D로 변환
    book_time.forEach(time => {
        const start = time[0].slice(0,5).split(':').map(num => Number(num))
        const end = time[1].slice(0,5).split(':').map(num => Number(num))
        
        times.push([start, end])
    })
    
    // 예약 시간이 빠른 순으로 정렬
    times.sort((a, b)=> {
        const [[hourStartA, minuteStartA], [hourEndA, minuteEndA]] = a
        const [[hourStartB, minuteStartB], [hourEndB, minuteEndB]] = b
        
        if (hourStartA !== hourStartB) return hourStartA - hourStartB
        if (hourStartA === hourStartB) return minuteStartA - minuteStartB
        
        return hourEndA - hourEndB
    })
    
    // 예약 시간 탐색
    times.map(time => {
        const [start, end] = time
        
        // 예약 후 새로운 rooms 할당
        rooms = getRoom(start, end, rooms)
    })

    // 객실의 수
    answer = rooms.length
    
    return answer;
}