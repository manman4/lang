function isPrime(n) {
    if (n < 2)
        return false;
    if (n === 2)
        return true;
    if (n % 2 === 0)
        return false;
    for (var i = 3; i * i <= n; i += 2) {
        if (n % i === 0)
            return false;
    }
    return true;
}
function nthPrime(n) {
    var count = 0;
    var num = 1;
    while (count < n) {
        num++;
        if (isPrime(num))
            count++;
    }
    return num;
}
// 例: 10 番目の素数を求める
console.log(nthPrime(10)); // 29
