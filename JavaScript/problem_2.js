function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;
  
  memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
  return memo[num]
}

function euler2(limit){  
    fibonacciNumbers = {}
    let num, sum;
    num = 2;
    sum = 0;
    currentFib = fibonacci(num, fibonacciNumbers);
    while (currentFib <= limit){
        if (currentFib % 2 === 0){
            sum += currentFib;
        }
        num += 1;
        currentFib = fibonacci(num, fibonacciNumbers);
        //console.log(currentFib)
    }
    return sum

}    
console.log(euler2(4000000));