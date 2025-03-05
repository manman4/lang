function fibonacci(n, memo) {
    if (memo === void 0) { memo = {}; }
    if (n in memo)
        return memo[n];
    if (n <= 1)
        return n;
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}
// 例: 0 から 10 までのフィボナッチ数を計算
for (var i = 0; i <= 10; i++) {
    console.log("F(".concat(i, ") = ").concat(fibonacci(i)));
}
