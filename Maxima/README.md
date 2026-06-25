# Maxima

## インストール

### Mac

brew install maxima


## マニュアル

http://fe.math.kobe-u.ac.jp/MathLibre-doc/maxima-note.pdf

## ファイルの実行

### コマンドラインから

```bash
# バッチ実行（結果を表示して終了）
maxima --batch=yourfile.mac

# 静かに実行
maxima --quiet --batch=yourfile.mac
```

### 対話セッション内から

```maxima
/* ファイルを読み込んで実行（結果を表示） */
batch("yourfile.mac");

/* 関数定義などの読み込み（出力なし） */
load("yourfile.mac");
```

| コマンド | 用途 |
|---------|------|
| `batch()` | 実行して各式の結果を表示 |
| `load()` | 関数定義やパッケージの読み込み（出力なし） |
| `batchload()` | `batch()`と似ているが最後の値を返す |

ファイル拡張子は `.mac` が一般的。

