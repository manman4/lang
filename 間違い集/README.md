# やりがちな間違い

リストのコピー

https://twitter.com/miyashin_prg/status/1546978955944607744

```python
>>> a=[1]
>>> b=[1,2]
>>> a=b
>>> a.append(3)
>>> b
[1, 2, 3]
>>> a=[1]
>>> b=[2,3]
>>> a=b
>>> a.append(0)
>>> b
[2, 3, 0]
>>>
```

rubyも同じ挙動をする。 これにループが混じるとややこしい。

```ruby
a = []
ary = []
5.times{|i|
  a << i
  b = [i]
  a = b
  ary << b
}
p ary
```

```ruby
a = []
ary = []
5.times{|i|
  a << i
  b = [i]
  a = b
  ary << [b.inject(:+)]
}
p ary
```

それぞれの結果は異なる。　それぞれ、[[0, 1], [1, 2], [2, 3], [3, 4], [4]]と[[0], [1], [2], [3], [4]]


