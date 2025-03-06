function isPrime(n: number): boolean {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

// テスト: 1〜20 の数が素数かどうか判定
for (let i = 1; i <= 20; i++) {
    console.log(`${i} is prime? ${isPrime(i)}`);
}
