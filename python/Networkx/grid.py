import networkx as nx
import random
import matplotlib.pyplot as plt

# グラフを作成する長方形の辺の長さを指定
n = 20
m = 10

#グラフを作る
G = nx.Graph()

#確率0.5でノードを追加
for i in range(n):
    for j in range(m):
        rate = random.random()
        if rate >= 0.5:
            G.add_node((i, j))

#行方向にエッジを追加
for i in range(n):
    for j in range(m-1):
        if (i,j) in G and (i,j+1) in G:
            G.add_edge((i, j), (i, j+1))

#列方向にエッジを追加
for j in range(m):
    for i in range(n-1):
        if (i,j) in G and (i+1,j) in G:
            G.add_edge((i, j), (i+1, j))

#ノードから出ているエッジが多いほどノードの描画サイズを大きくする
node_size = [10*len(G[i]) for i in G.nodes()]
#ノードから出ているエッジが３つ以上であれば赤色でノードを描画する
node_color = ['red' if len(G[i]) >= 3 else 'blue' for i in G.nodes()]

pos = {n: (n[1], n[0]) for n in G.nodes()}
nx.draw_networkx_nodes(G, pos, node_size=node_size, alpha=1, node_color=node_color)
nx.draw_networkx_edges(G, pos, label=1, edge_color="black", width=2)
plt.savefig('graph_sample.png')

