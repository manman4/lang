# Sage

## インストール

### Mac

久しぶりにMacでSageを使おうとしたら、インストールのファイルが分かりにくかったのでメモ。

以下のサイトから、ダウンロードする。

https://github.com/3-manifolds/Sage_macOS/releases


## ファイルによる実行

インタラクティブモードで開かず、普通にターミナルから

sage xxx.sage

で実行できる。

ただし、以下の通り自動的に xxx.sage.pyが生成される

https://ask.sagemath.org/question/38383/suppress-automatically-generated-python-files-when-running-sage-script/

## 包含しているsoft

https://doc.sagemath.org/html/ja/tutorial/interfaces.html

PARI, GAP, Singular, Maxima


## 計算

### 型

PARI/GP は「型を意識せずとも高精度の整数・有理数演算が自然に行える」設計だが、明示的な型を意識しないと意図しない精度落ちが発生

ex. q_binomial のような関数では、q の型により返り値の型が変化する

### 第１種スターリング数

PARIと違い符号なし

```Sage:
sage: print([stirling_number1(9, n) for n in (0..9)])
# [0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1]
```
