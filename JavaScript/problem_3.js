function isPrime (num) {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++)
        if(num % i === 0) return false; 
    return num > 1;
}

function euler3(num){
    for (var i = num; i >= 0; i--) {
	if ((num % i === 0) && (isPrime(i))){
        return i;
    }
}
}

//console.log(maxPrimeDivisor(600851475143));
console.log(euler2(600851475143));