# 🚀 lang ✨

言語の比較等行う。

自分用辞書

環境構築は「environment_setup」でまとめている。

## 対象言語

Go, Python, julia, Ruby, Crystal, Java

### 高度な言語

PARI, SageMath, Singular


--------------------

インデント

| インデント | Python | Ruby | Go | C | C++ | Pari/GP |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| - | 4スペース | 2スペース | タブ | 4スペース | 4スペース | 2スペース(or4スペース) |


--------------------

文字列の操作

| 操作 | Go | Ruby |
| :--: | :--: | :--: |
| 数字へ | n, _ = strconv.Atoi(s) | n = s.to_i |
| 文字へ | s = strconv.Itoa(n) | i = n.to_s |

--------------------

繰り返し

| 言語 | Python | Ruby |
| :--: | :--: | :--: |
|  break（あるいは return）されなかったら何かを実行 | for else | なし？ | 

--------------------

クラスメソッドとスタティックメソッド

| 言語 | Python | Ruby | Java |
| :--: | :--: | :--: | :--: |
| クラスメソッド | あり | あり | なし | 
| スタティックメソッド | あり | なし | あり |

--------------------

便利

| 言語 | Python | Ruby | PARI |
| :--: | :--: | :--: | :--: |
| apply | pandas あり | ? | あり | 

```PARI:apply
my(x='x+O('x^30)); apply(round, Vec(serlaplace(cosh(sqrt(3)*(exp(x)-1)))))
```


