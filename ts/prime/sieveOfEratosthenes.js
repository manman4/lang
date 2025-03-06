function sieveOfEratosthenes(limit) {
    var primes = [];
    for (var i = 0; i <= limit; i++) {
        primes[i] = true;
    }
    primes[0] = primes[1] = false;
    for (var i = 2; i * i <= limit; i++) {
        if (primes[i]) {
            for (var j = i * i; j <= limit; j += i) {
                primes[j] = false;
            }
        }
    }
    return primes.map(function (isPrime, index) { return isPrime ? index : -1; }).filter(function (n) { return n !== -1; });
}
// 例: 100 以下の素数を求める
console.log(sieveOfEratosthenes(100));
