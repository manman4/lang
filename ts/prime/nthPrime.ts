function isPrime(n: number): boolean {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

function nthPrime(n: number): number {
    let count = 0;
    let num = 1;

    while (count < n) {
        num++;
        if (isPrime(num)) count++;
    }
    return num;
}

// 例: 10 番目の素数を求める
console.log(nthPrime(10)); // 29
