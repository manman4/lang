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

pos = {n: (n[1], n[0]) for n in G.nodes()}
nx.draw_networkx_nodes(G, pos, node_size=30, alpha=1, node_color='blue')
nx.draw_networkx_edges(G, pos, label=1, edge_color="black", width=2)
plt.savefig('graph_sample.png')

