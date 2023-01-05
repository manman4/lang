# 便利なツール

## 計算

- [Graphillion](https://github.com/takemaru/graphillion/wiki)

用途：グラフがらみ

OS：Linux, Mac

## 数理最適

- Gurobi ソルバー

https://qiita.com/virtualnkhr_/items/8665627403d153d65246

1. conda config --add channels https://conda.anaconda.org/gurobi 
2. conda install gurobi

## 描画

- matplotlib

- folium  マップ表示

- japanmap  白地図

- pyplot  グラフ

- altair  グラフ

## 画像処理

- OpenCV

## 機械学習

- scikit-learn

- TensorFlow

- PyTorch

## サーバ

- pings

AttributeError: module ‘time’ has no attribute ‘clock’への対処

https://obenkyolab.com/?p=2817

~\site-packages\pingsping.pyを開き、該当箇所のtime.clockをtime.timeに変更。

