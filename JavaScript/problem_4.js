function isPalindrome(s){
    return (s === s.split('').reverse().join(''))
}

function euler4(limit){
    let result, temp, storeM, storeN;
    result = 0;
    temp = 0; 
    for (let n = 100; n <= limit; n++){
        for(let m = 100; m <= Math.min(Math.floor((limit * limit)/n), limit); m++){
            temp = m * n;
            if((isPalindrome(temp.toString()) && (temp > result))){
                storeM = m;
                storeN = n;
                result = temp;
            }
        }
    }
    return result;
}

console.log(euler4(999));