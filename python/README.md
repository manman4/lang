## opencv は別repository

## debug

```
import pdb;

# 止めたいところ
pdb.set_trace()
```

## コード規約

### black

```
find . -name "*.py" -exec black {} \;  # 1つずつ処理
find . -name "*.py" -exec black {} +   # 複数まとめて処理（推奨）
```


## version による違い

### メモ化

3.9以降は書き方が少し簡単になった。

https://www.youtube.com/watch?v=dpuykHkw8QM
