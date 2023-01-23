function solution(clothes) {
    let answer = 1;
    const clothes_category = {}
    
    clothes.forEach((e) => {
        const category = e[1]
        
        
        if (clothes_category[category] === undefined) {
            clothes_category[category] = [e[0]]
        } else {
            clothes_category[category].push(e[0])
        }
    })

    for (const [key, value] of Object.entries(clothes_category)) {
        answer *= (value.length + 1)
    }
    
    return (answer - 1);
}