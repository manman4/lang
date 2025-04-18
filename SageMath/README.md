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

### 第１種スターリング数

PARIと違い符号なし

```Sage:
sage: print([stirling_number1(9, n) for n in (0..9)])
# [0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1]
```
