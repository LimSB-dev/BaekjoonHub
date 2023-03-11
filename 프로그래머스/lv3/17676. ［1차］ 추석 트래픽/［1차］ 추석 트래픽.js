function solution(lines) {
  const timeLogs = lines.map((line) => {
    const [date, time, duration] = line.split(" ");
    const endDate = new Date(`${date}T${time}`);
    const durationMs = parseFloat(duration.replace("s", "")) * 1000;
    const startDate = new Date(endDate.getTime() - durationMs + 1); // 시작 시간 계산
    return [startDate.getTime(), endDate.getTime()];
  });

  let maxCount = 0;
  for (let i = 0; i < timeLogs.length; i++) {
    const curEndTime = timeLogs[i][1];
    let curCount = 0;
    for (let j = 0; j < timeLogs.length; j++) {
      const [start, end] = timeLogs[j];
      if (start < curEndTime + 1000 && end >= curEndTime) {
        curCount++;
      }
    }
    maxCount = Math.max(maxCount, curCount);
  }
  return maxCount;
}
