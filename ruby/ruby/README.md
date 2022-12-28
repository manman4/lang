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


```
$ echo $SHELL
```

/bin/zshの場合

```
$ echo 'eval "$(rbenv init -)"' >>  ~/.zshrc
$ source ~/.zshrc
$ ruby --version
```


# 小ネタ

```Ruby
# "a\r\nb\rc\n".split(/\r\n|\r|\n/)でなく
"a\r\nb\rc\n".split(/\R/)
=> ["a", "b", "c"]
```
