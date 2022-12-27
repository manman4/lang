# インストール

最近遅いらしい。

https://blog.manabusakai.com/2020/01/no-longer-depends-on-homebrew-openssl/

# 小ネタ

```Ruby
# "a\r\nb\rc\n".split(/\r\n|\r|\n/)でなく
"a\r\nb\rc\n".split(/\R/)
=> ["a", "b", "c"]
```
