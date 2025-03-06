function sieveOfEratosthenes(limit: number): number[] {
    const primes: boolean[] = [];
    for (let i = 0; i <= limit; i++) {
        primes[i] = true;
    }
    primes[0] = primes[1] = false;

    for (let i = 2; i * i <= limit; i++) {
        if (primes[i]) {
            for (let j = i * i; j <= limit; j += i) {
                primes[j] = false;
            }
        }
    }

    return primes.map((isPrime, index) => isPrime ? index : -1).filter(n => n !== -1);
}

// 例: 100 以下の素数を求める
console.log(sieveOfEratosthenes(100));
