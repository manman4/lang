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
// テスト: 1〜20 の数が素数かどうか判定
for (var i = 1; i <= 20; i++) {
    console.log("".concat(i, " is prime? ").concat(isPrime(i)));
}
