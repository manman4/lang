using Primes


n = 101
is_prime_result = isprime(n)

if is_prime_result
    println("$n は素数です。")
else
    println("$n は素数ではありません。")
end


n = 202112271521
factors = factor(n)
println("202112271521の素因数分解: $n = $factors")