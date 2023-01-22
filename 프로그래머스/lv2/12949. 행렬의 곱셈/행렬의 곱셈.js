function solution(arr1, arr2) {
    const anwer = [];

    for(let i = 0; i < arr1.length; i++) {
        let arr = [];
        for(let j = 0; j < arr2[0].length; j++) {
            let value = 0;
            for(let k = 0; k < arr2.length; k++) {
                value += arr1[i][k] * arr2[k][j];
            }
            arr.push(value);
        }
        anwer.push(arr);
    }
    return anwer;
}
