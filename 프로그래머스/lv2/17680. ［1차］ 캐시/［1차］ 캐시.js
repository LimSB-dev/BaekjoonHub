function solution(cacheSize, cities) {
    let answer = 0;
    const cache = [];

    cities.forEach((city) => {
        city = city.toLowerCase();
        
        if(cache.includes(city)) {
            answer++;
            cache.splice(cache.indexOf(city),1);
        } else {
            answer += 5;
        }
        
        cache.push(city);
        
        if(cache.length > cacheSize) cache.shift();
    })

    return answer;
}