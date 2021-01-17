# 小ネタ

```Ruby
# "a\r\nb\rc\n".split(/\r\n|\r|\n/)でなく
"a\r\nb\rc\n".split(/\R/)
=> ["a", "b", "c"]
```