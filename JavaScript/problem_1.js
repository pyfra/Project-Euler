function sumMultipleOfN(num, n){
    let i, sum = 0;
    for (i = n; i < num; i += n) {
        if (i % n === 0) {
            sum += i;
        }
    }
    return sum
}

function euler01(num) {
    console.log(sumMultipleOfN(num, 3) + sumMultipleOfN(num, 5) - sumMultipleOfN(num, 15))
}

console.log(euler01(1000));
