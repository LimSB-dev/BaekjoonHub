function solution(sizes) {
    var max_w = 0;
    var max_h = 0;
    for (size of sizes) {
        
        if (size[0] > size[1]) {
            
            let tmp = size[1];
            size[1] = size[0];
            size[0] = tmp
            
        };
        
        if (size[0] > max_w) {
            max_w = size[0]
        };
            
        if (size[1] > max_h) {
            max_h = size[1]
        };
    };
    
    var answer = max_w * max_h;
    return answer;
}