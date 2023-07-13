from datetime import datetime, timedelta

def solution(lines):
    timeLogs = []
    for line in lines:
        date, time, duration = line.split(" ")
        endDate = datetime.strptime(date + "T" + time, "%Y-%m-%dT%H:%M:%S.%f")
        durationMs = float(duration[:-1]) * 1000
        startDate = endDate - timedelta(milliseconds=durationMs) + timedelta(milliseconds=1)
        timeLogs.append([startDate.timestamp() * 1000, endDate.timestamp() * 1000])
    
    maxCount = 0
    for i in range(len(timeLogs)):
        curEndTime = timeLogs[i][1]
        curCount = 0
        for j in range(len(timeLogs)):
            start, end = timeLogs[j]
            if start < curEndTime + 1000 and end >= curEndTime:
                curCount += 1
        maxCount = max(maxCount, curCount)
    
    return maxCount
