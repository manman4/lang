# インストール

最近遅いらしい。

https://blog.manabusakai.com/2020/01/no-longer-depends-on-homebrew-openssl/

一応インストール方法

```
brew upgrade rbenv ruby-build
rbenv install --list
rbenv install 3.1.2
rbenv global 3.1.2
rbenv versions
```

Rubyのバージョンが切り替わらない時

https://qiita.com/opiyo_taku/items/3312a75d5916f6cd32b1

```
$ vi ~/.bash_profile
export PATH="~/.rbenv/shims:/usr/local/bin:$PATH"
eval "$(rbenv init -)"
$ source ~/.bash_profile
```


# 小ネタ

```Ruby
# "a\r\nb\rc\n".split(/\r\n|\r|\n/)でなく
"a\r\nb\rc\n".split(/\R/)
=> ["a", "b", "c"]
```
